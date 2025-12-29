#!/usr/bin/env python3
"""
Matplotlib Bar Chart Template
For performance comparisons and categorical data

Usage:
    python matplotlib-bar-chart-template.py
"""

import matplotlib.pyplot as plt
import numpy as np

# ============================================
# CONFIGURATION
# ============================================

COLORS = {
    'primary':    '#1a5f7a',
    'secondary':  '#57837b',
    'accent':     '#c4dfdf',
    'highlight':  '#f26b60',
    'success':    '#28a745',
    'warning':    '#ffc107',
    'danger':     '#dc3545',
}

FIGSIZE = (10, 6)
DPI = 150

# ============================================
# DATA
# ============================================

categories = ['RSA-1024', 'RSA-2048', 'RSA-4096', 'ECC-256', 'ECC-384', 'ECC-521']
values = [10, 45, 180, 5, 8, 12]  # Example: Time in milliseconds

# Optional: Color per category
bar_colors = [
    COLORS['primary'],    # RSA-1024
    COLORS['primary'],    # RSA-2048
    COLORS['primary'],    # RSA-4096
    COLORS['secondary'],  # ECC-256
    COLORS['secondary'],  # ECC-384
    COLORS['secondary'],  # ECC-521
]

# Highlight the best/fastest
highlight_index = 3  # ECC-256
bar_colors[highlight_index] = COLORS['highlight']

# ============================================
# PLOTTING
# ============================================

fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)

# Create bar chart
bars = ax.bar(categories, values, color=bar_colors, alpha=0.8, edgecolor='white', linewidth=1.5)

# Add value labels on top of bars
for i, (bar, value) in enumerate(zip(bars, values)):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{value} ms',
            ha='center', va='bottom',
            fontsize=10, fontweight='bold')

# ============================================
# STYLING
# ============================================

ax.set_ylabel('Time (milliseconds)', fontsize=12, fontweight='bold')
ax.set_xlabel('Algorithm', fontsize=12, fontweight='bold')
ax.set_title('Key Generation Performance Comparison', fontsize=14, fontweight='bold', pad=20)

# Grid (only horizontal for bar charts)
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)  # Grid behind bars

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Rotate x-axis labels if needed
plt.xticks(rotation=45, ha='right')

# Optional: Add legend for categories
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=COLORS['primary'], label='RSA'),
    Patch(facecolor=COLORS['secondary'], label='ECC'),
    Patch(facecolor=COLORS['highlight'], label='Best Performance')
]
ax.legend(handles=legend_elements, loc='upper left', framealpha=0.9)

plt.tight_layout()

# ============================================
# SAVE
# ============================================

output_filename = 'chXX-figYY-performance-comparison.png'

plt.savefig(output_filename,
            dpi=300,
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none')

print(f"Figure saved as: {output_filename}")
plt.show()
plt.close()
