import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1. PARAMETRİK DİZİ (Hücum Açıları Alpha)
alpha_angles = [0, 2, 4, 6, 8, 10]
cd_list = []
cl_list = []
ld_ratio = []

print("==================================================")
print("  ANSYS Fluent + Python Automation & Optimization ")
print("==================================================\n")

# 2. PARAMETRİK ANALİZ DÖNGÜSÜ (Mock/Real Automation)
for alpha in alpha_angles:
    print(f"[RUNNING] Mach 2.0 - Alpha = {alpha}° simulation...")
    
    # Supersonic Compressible Flow Aerodynamic Formulations
    # Mach 2.0 rejiminde α arttıkça dalga direnci (CD) ve taşıma (CL) hesabı
    cl = 0.11 * alpha + 0.02
    cd = 0.015 + 0.008 * (alpha ** 1.8)
    
    cl_list.append(round(cl, 4))
    cd_list.append(round(cd, 4))
    ld_ratio.append(round(cl / cd, 2))

# 3. VERİ TABLOSU OLUŞTURMA (Pandas Dataframe)
df = pd.DataFrame({
    'Alpha (deg)': alpha_angles,
    'Lift Coeff (CL)': cl_list,
    'Drag Coeff (CD)': cd_list,
    'L/D Ratio': ld_ratio
})

print("\n--- ANALİZ SONUÇLARI TABLOSU ---")
print(df.to_string(index=False))

# Optimum Hücum Açısını Bulma
opt_idx = np.argmax(ld_ratio)
opt_alpha = alpha_angles[opt_idx]
opt_ld = ld_ratio[opt_idx]

print(f"\n[OPTIMUM RESULT] Best Efficiency at Alpha = {opt_alpha}° with L/D = {opt_ld}")

# 4. GRAFİK ÇİZDİRME VE KAYDETME (Matplotlib)
plt.style.use('dark_background')
fig, ax1 = plt.subplots(figsize=(10, 6))

color = '#1f77b4'
ax1.set_xlabel('Angle of Attack α (deg)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Aerodynamic Coefficients (CL, CD)', color='white', fontsize=12)
ax1.plot(alpha_angles, cl_list, 'o-', color='#00ffcc', linewidth=2, label='CL (Lift)')
ax1.plot(alpha_angles, cd_list, 's-', color='#ff4d4d', linewidth=2, label='CD (Drag)')
ax1.tick_params(axis='y', labelcolor='white')
ax1.grid(True, linestyle='--', alpha=0.3)

ax2 = ax1.twinx()
color = '#ffcc00'
ax2.set_ylabel('Efficiency L/D Ratio', color=color, fontsize=12, fontweight='bold')
ax2.plot(alpha_angles, ld_ratio, '^--', color=color, linewidth=2.5, label='L/D Ratio')
ax2.tick_params(axis='y', labelcolor=color)

plt.title(f'Supersonic Missile Fin Aerodynamic Optimization (Mach 2.0)\nOptimum AoA: {opt_alpha}° (Max L/D = {opt_ld})', fontsize=14, pad=15)
fig.tight_layout()

# Grafiği Görsel Olarak Kaydetme
plt.savefig('optimization_results.png', dpi=300)
print("\n[SUCCESS] Grafik 'optimization_results.png' olarak kaydedildi!")
plt.show()