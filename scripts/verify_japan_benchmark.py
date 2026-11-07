"""
SMI Framework: Empirical Benchmark Verification Script (Japan 1970-2024)
Calculates effective SMI against official Vital Statistics TFR with a 4-year lag.
"""

import numpy as np
import pandas as pd
from scipy.interpolate import pchip_interpolate
from scipy.stats import pearsonr

# 1. Historical Benchmark Data (Official Statistics: e-Stat / MHLW / Statistics Bureau)
benchmark_points = [
    # Year, WCI (10k JPY), C_base (10k JPY), TFR (Observed)
    (1970, 4.5,  1.9, 2.13),
    (1975, 9.8,  4.2, 1.91),
    (1980, 14.2, 7.1, 1.75),
    (1985, 18.5, 9.8, 1.76),
    (1990, 22.8, 13.5, 1.54),
    (1995, 24.5, 17.2, 1.42),
    (1997, 24.8, 19.5, 1.39), # Crucial inflection: Tax & Social Insurance reform
    (2000, 23.5, 21.0, 1.36),
    (2005, 22.0, 22.8, 1.26),
    (2010, 21.5, 24.2, 1.39),
    (2015, 22.5, 26.5, 1.45),
    (2020, 23.0, 29.8, 1.33),
    (2024, 23.8, 33.2, 1.15)
]

df_raw = pd.DataFrame(benchmark_points, columns=['year', 'wci', 'c_base', 'tfr'])
years_full = np.arange(1970, 2025)

# 2. Monotonic Interpolation (PCHIP)
wci_interp = pchip_interpolate(df_raw['year'], df_raw['wci'], years_full)
c_base_interp = pchip_interpolate(df_raw['year'], df_raw['c_base'], years_full)
tfr_interp = pchip_interpolate(df_raw['year'], df_raw['tfr'], years_full)

smi_interp = wci_interp / c_base_interp

df = pd.DataFrame({
    'year': years_full,
    'SMI': smi_interp,
    'TFR': tfr_interp
})

# 3. 4-Year Distributed Phase Delay Analysis (Lag = 4 years)
df['TFR_lead4'] = df['TFR'].shift(-4)
valid = df.dropna(subset=['SMI', 'TFR_lead4'])

r_val, p_val = pearsonr(valid['SMI'], valid['TFR_lead4'])
r2 = r_val ** 2

print("=" * 60)
print(" SMI Framework: Japan Empirical Transfer Verification")
print("=" * 60)
print(f"Sample Interval           : 1970 - 2020 (Shifted Horizon)")
print(f"Phase Lag Applied         : 4.0 Years (t + 4)")
print(f"Pearson Correlation (r)   : {r_val:.4f}")
print(f"Coefficient of Determ (R²): {r2:.4f}")
print(f"Statistical Significance  : p = {p_val:.4e}")
print("=" * 60)
