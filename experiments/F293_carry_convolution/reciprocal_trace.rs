use std::time::Instant;

fn inverse_odd(a: u64, mask: u64) -> u64 {
    let mut inverse = 1u64;
    for _ in 0..6 {
        inverse = inverse.wrapping_mul(2u64.wrapping_sub(a.wrapping_mul(inverse)));
    }
    inverse & mask
}

fn power(mut base: u64, mut exponent: u64, mask: u64) -> u64 {
    let mut result = 1u64;
    while exponent != 0 {
        if exponent & 1 != 0 {
            result = result.wrapping_mul(base) & mask;
        }
        base = base.wrapping_mul(base) & mask;
        exponent >>= 1;
    }
    result
}

fn main() {
    // A bounded exact experiment, not a succinct coefficient evaluator.
    // One process, constant memory, 25-second internal limit.
    let started = Instant::now();
    let mut total_iterations = 0u64;
    for k in 4..=34u32 {
        let modulus = 1u64 << k;
        let mask = modulus - 1;
        let half = modulus / 2;
        let quarter_period = modulus / 16;
        for target in [1u64, 3, 5] {
            let case_started = Instant::now();
            let sign = if target % 4 == 1 { 1i64 } else { -1i64 };
            let principal = if sign == 1 { target } else { modulus - target };
            // Bit lifting of the known power-of-two cyclic-group logarithm.
            let mut index = 0u64;
            let mut current = 1u64;
            let mut step = 5u64;
            for bit in 0..k - 2 {
                let small_mask = (1u64 << (bit + 3)) - 1;
                if current & small_mask != principal & small_mask {
                    index += 1u64 << bit;
                    current = current.wrapping_mul(step) & mask;
                }
                step = step.wrapping_mul(step) & mask;
            }
            assert_eq!(current, principal);
            let length = if index % 2 == 0 { quarter_period - 1 } else { quarter_period };
            let start = index / 2 + 1;
            let mut u = power(5, start, mask);
            let mut v = principal.wrapping_mul(inverse_odd(u, mask)) & mask;
            let inv5 = inverse_odd(5, mask);
            let mut sum = 0i64;
            for j in 0..length {
                if j & ((1 << 18) - 1) == 0 && started.elapsed().as_secs_f64() > 25.0 {
                    println!("{{\"status\":\"budget_exhausted\",\"k\":{k},\"N\":{target},\"partial_iterations\":{j},\"total_completed_iterations\":{total_iterations}}}");
                    return;
                }
                sum += if (u < half) == (v < half) { 1 } else { -1 };
                u = u.wrapping_mul(5) & mask;
                v = v.wrapping_mul(inv5) & mask;
            }
            let convolution = 4 * sum;
            let count = (modulus / 8) as i64 + 2 * sign * sum;
            if k <= 12 {
                let direct = (1..half).step_by(2).filter(|&x| {
                    target.wrapping_mul(inverse_odd(x, mask)) & mask < half
                }).count() as i64;
                assert_eq!(count, direct);
            }
            total_iterations += length;
            println!("{{\"status\":\"complete\",\"k\":{k},\"N\":{target},\"half_square_count\":{count},\"signed_convolution\":{},\"iterations\":{length},\"total_iterations\":{total_iterations},\"elapsed_seconds\":{:.9}}}", sign * convolution, case_started.elapsed().as_secs_f64());
        }
    }
    println!("{{\"status\":\"all_complete\",\"total_iterations\":{total_iterations},\"elapsed_seconds\":{:.9}}}", started.elapsed().as_secs_f64());
}
