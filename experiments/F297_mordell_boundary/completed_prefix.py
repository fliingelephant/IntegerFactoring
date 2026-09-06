"""F297: test the centered completed-prefix identity by independent quadrature."""

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
for t_q in (Q(1, 2), Q(1, 8), Q(3, 16)):
    t = mp.mpf(t_q.numerator) / t_q.denominator
    root = mp.exp(-mp.j * mp.pi / 4) * mp.sqrt(mp.pi / t)
    factor = mp.exp(mp.j * mp.pi / 4) / mp.sqrt(t)
    for alpha_q in (Q(0), Q(1, 4), Q(7, 8)):
        alpha = mp.mpf(alpha_q.numerator) / alpha_q.denominator
        common_z = alpha - t / 2 + mp.mpf("0.5")
        reduced_common = common_z - int(mp.floor(common_z + mp.mpf("0.5")))
        common_regular = 2 * mp.quad(
            lambda x: mp.exp(-2*x-mp.j*t*x*x/mp.pi)
            * mp.cosh(2*reduced_common*x) / mp.cosh(x), knots,
        )
        h_common = mp.exp(-mp.j*mp.pi/4)/mp.sqrt(t) * sum(
            mp.exp(-mp.j*mp.pi*d*d/t)*mp.erfc(root*d)
            for d in (mp.mpf("0.5") + reduced_common, mp.mpf("0.5") - reduced_common)
        ) - common_regular/mp.pi
        if common_z != reduced_common:
            assert abs(common_z - reduced_common - 1) < mp.mpf("1e-35")
            h_common = (2*mp.exp(-mp.j*mp.pi/4)/mp.sqrt(t)
                        * mp.exp(-mp.j*mp.pi*(common_z-mp.mpf("0.5"))**2/t)
                        - h_common)
        common = -mp.j/2 * mp.exp(-mp.j*mp.pi*(alpha-t/4)) * h_common
        for n in (0, 1, 3, 9, 17):
            X_q = Q(2*n+1, 2)
            r = (alpha_q+t_q*X_q).__floor__()
            d_q = alpha_q+t_q*X_q-r
            d = mp.mpf(d_q.numerator) / d_q.denominator
            z = d-mp.mpf("0.5")
            X = mp.mpf(n)+mp.mpf("0.5")
            g_r = mp.exp(-mp.j*mp.pi*(alpha-r)**2/t)
            g_next = mp.exp(-mp.j*mp.pi*(alpha-r-1)**2/t)
            E = (-1)**r*mp.exp(2*mp.j*mp.pi*(alpha*X+t*X*X/2))
            regular = 2*mp.quad(
                lambda x: mp.exp(-2*x-mp.j*t*x*x/mp.pi)
                * mp.cosh(2*z*x) / mp.cosh(x), knots,
            )
            dual = factor*sum(mp.exp(-mp.j*mp.pi*(alpha-k)**2/t) for k in range(r+1))
            endpoints = factor/2 * (-g_r*mp.erfc(root*d) + g_next*mp.erfc(root*(1-d)))
            regular_term = mp.j/(2*mp.pi)*E*regular
            direct = sum(mp.exp(2*mp.j*mp.pi*(alpha*k+t*k*k/2)) for k in range(n+1))
            corrected = dual+common+endpoints+regular_term
            # The cached equation (7) prints -1/2 for its second term.
            # Retain that expression separately; the derived coefficient is -i/2.
            printed = dual+common+(endpoints+regular_term)/mp.j
            error = abs(direct-corrected)
            assert error < mp.mpf("1e-30"), (t_q, alpha_q, n, error)
            rows.append({"t":str(t_q), "alpha":str(alpha_q), "n":n, "r":r,
                         "d":str(d_q), "corrected_error":mp.nstr(error,20),
                         "printed_expression_error":mp.nstr(abs(direct-printed),20)})

result = {"status":"complete", "family":"route:F31", "checks":rows,
          "scope":"Numerical identity comparisons at 42 decimal digits, not a proof of quadrature accuracy.",
          "runtime_seconds":time.monotonic()-started,
          "peak_rss_bytes":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"status":"complete", "comparisons":len(rows),
                  "max_corrected_error":max(float(row["corrected_error"]) for row in rows),
                  "max_printed_error":max(float(row["printed_expression_error"]) for row in rows),
                  "runtime_seconds":result["runtime_seconds"],"peak_rss_bytes":result["peak_rss_bytes"]}))
