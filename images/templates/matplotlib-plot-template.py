#!/usr/bin/env python3
"""
Matplotlib Plot Template
For creating consistent, professional plots in the ebook

Usage:
    python matplotlib-plot-template.py
"""

import matplotlib.pyplot as plt
import numpy as np

# ============================================
# CONFIGURATION
# ============================================

# Poltek SSN Color Palette
COLORS = {
    'primary':    '#1a5f7a',  # Dark teal - Main elements
    'secondary':  '#57837b',  # Medium teal - Secondary elements
    'accent':     '#c4dfdf',  # Light teal - Backgrounds
    'highlight':  '#f26b60',  # Coral red - Important highlights
    'success':    '#28a745',  # Green - Success states
    'warning':    '#ffc107',  # Yellow - Warnings
    'danger':     '#dc3545',  # Red - Errors, critical
}

# Figure settings
FIGSIZE = (10, 6)
DPI = 150  # For display (use 300 for saving)
FONT_SIZE = {
    'title': 14,
    'label': 12,
    'tick': 10,
    'legend': 11
}

# ============================================
# DATA PREPARATION
# ============================================

# Example data - replace with your actual data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# ============================================
# PLOTTING
# ============================================

fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)

# Plot data
ax.plot(x, y1, color=COLORS['primary'], linewidth=2.5, label='Function 1', marker='o', markersize=4, markevery=10)
ax.plot(x, y2, color=COLORS['secondary'], linewidth=2.5, label='Function 2', marker='s', markersize=4, markevery=10)

# Optional: Add important points
# ax.plot(5, 0, 'o', color=COLORS['highlight'], markersize=10, zorder=5, label='Critical Point')

# ============================================
# STYLING
# ============================================

# Labels and title
ax.set_xlabel('X-axis Label', fontsize=FONT_SIZE['label'], fontweight='bold')
ax.set_ylabel('Y-axis Label', fontsize=FONT_SIZE['label'], fontweight='bold')
ax.set_title('Plot Title', fontsize=FONT_SIZE['title'], fontweight='bold', pad=20)

# Grid
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

# Remove top and right spines for cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Legend
ax.legend(fontsize=FONT_SIZE['legend'], loc='best', framealpha=0.9)

# Tick parameters
ax.tick_params(axis='both', labelsize=FONT_SIZE['tick'])

# Optional: Set axis limits
# ax.set_xlim(0, 10)
# ax.set_ylim(-1.5, 1.5)

# Tight layout
plt.tight_layout()

# ============================================
# SAVE FIGURE
# ============================================

output_filename = 'chXX-figYY-description.png'

plt.savefig(output_filename,
            dpi=300,  # Publication quality
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none')

print(f"Figure saved as: {output_filename}")

# Display (comment out for batch processing)
plt.show()

# Clean up
plt.close()
