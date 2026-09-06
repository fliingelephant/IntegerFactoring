"""F297: absorb the exact nested-floor correction into four endpoint terms.

Resource estimate: one process, <128 MiB, <15 seconds; 45-second alarm.
Preflight at05:20: load1.84/2.15/2.07,72% available memory, no math process.
"""

import json
import resource
import signal
import time
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

signal.alarm(45)
started = time.monotonic()
mp.mp.dps = 42
knots = list(range(0, 41, 2))
rows = []
families = []


def regular_part(z, t):
    return 2*mp.quad(lambda x: mp.exp(-4*x-mp.j*t*x*x/mp.pi)
                     *mp.cosh(2*z*x)/mp.cosh(x), knots)


for m, A, B, a, b, z_sign in ((8, 1, 7, 5, 2, -1), (16, 3, 6, 13, 9, 1)):
    p = 2*A
    alpha_q, t_q = Q(B, m), Q(p, m)
    alpha, t = mp.mpf(B)/m, mp.mpf(p)/m
    Z = mp.exp(z_sign*2*mp.j*mp.pi/m)
    H = (a*(m-1)+b)//m
    c = -b-1
    k = (p*c+a*(B+A))//m
    eta = mp.exp(-mp.j*mp.pi/4)*mp.sqrt(mp.pi/t)
    Lambda = mp.exp(mp.j*mp.pi/4)/mp.sqrt(t)
    common_z = alpha-t/2+mp.mpf("0.5")
    h_common = mp.exp(-mp.j*mp.pi/4)/mp.sqrt(t)*sum(
        (-1)**ell*mp.exp(-mp.j*mp.pi*d*d/t)*mp.erfc(eta*d)
        for ell in range(2)
        for d in (common_z+ell+mp.mpf("0.5"), -common_z+ell+mp.mpf("0.5"))
    ) + regular_part(common_z, t)/mp.pi
    C0 = -mp.j/2*mp.exp(-mp.j*mp.pi*(alpha-t/4))*h_common
    total_direct, total_completed, total_uncorrected_bulk = mp.mpc(0), mp.mpc(0), mp.mpc(0)
    delta_positions = []
    for j in range(1, H+1):
        n = (m*j+c)//a
        X_q = Q(2*n+1, 2)
        r = (alpha_q+t_q*X_q).__floor__()
        R = (p*j+k)//a
        delta = R-r
        assert delta in (0, 1)
        if delta:
            delta_positions.append(j)
        d_q = alpha_q+t_q*X_q-R
        assert -1 <= d_q < 1
        d = mp.mpf(d_q.numerator)/d_q.denominator
        z = d-mp.mpf("0.5")
        X = mp.mpf(n)+mp.mpf("0.5")
        E = (-1)**R*mp.exp(2*mp.j*mp.pi*(alpha*X+t*X*X/2))
        direct = sum(mp.exp(2*mp.j*mp.pi*(alpha*h+t*h*h/2)) for h in range(n+1))
        bulk = Lambda*sum(mp.exp(-mp.j*mp.pi*(h-alpha)**2/t) for h in range(R+1))
        endpoints = Lambda/2*sum(
            -mp.exp(-mp.j*mp.pi*(R-ell-alpha)**2/t)*mp.erfc(eta*(d+ell))
            +mp.exp(-mp.j*mp.pi*(R+ell+1-alpha)**2/t)*mp.erfc(eta*(1-d+ell))
            for ell in range(2)
        )
        regular = -mp.j/(2*mp.pi)*E*regular_part(z, t)
        completed = bulk+C0+endpoints+regular
        error = abs(direct-completed)
        assert error < mp.mpf("1e-30"), (m,j,error)
        total_direct += Z**(j-1)*direct
        total_completed += Z**(j-1)*completed
        total_uncorrected_bulk += Z**(j-1)*bulk
        rows.append({"m":m,"j":j,"n":n,"r":r,"R":R,"delta":delta,
                     "d":str(d_q),"error":mp.nstr(error,22)})
    families.append({"m":m,"A":A,"B":B,"a":a,"b":b,"Z_sign":z_sign,
                     "delta_positions":delta_positions,
                     "direct_moment":str(total_direct),
                     "completed_moment":str(total_completed),
                     "bulk_before_endpoints":str(total_uncorrected_bulk),
                     "error":mp.nstr(abs(total_direct-total_completed),22)})

result = {"status":"complete","family":"route:F31","checks":rows,"families":families,
          "scope":"Exact endpoint selection plus high-precision numerical identity comparisons; quadrature is not interval-certified.",
          "runtime_seconds":time.monotonic()-started,
          "peak_rss_bytes":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"status":"complete","checks":len(rows),
                  "delta_positions":[family["delta_positions"] for family in families],
                  "max_error":max(float(row["error"]) for row in rows),
                  "runtime_seconds":result["runtime_seconds"],"peak_rss_bytes":result["peak_rss_bytes"]}))
