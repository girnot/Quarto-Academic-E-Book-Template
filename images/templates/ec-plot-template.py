#!/usr/bin/env python3
"""
Elliptic Curve Plot Template
For visualizing elliptic curves and point operations

Usage:
    python ec-plot-template.py
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
}

FIGSIZE = (10, 8)
DPI = 150

# ============================================
# ELLIPTIC CURVE FUNCTIONS
# ============================================

def plot_ec_real_field(a, b, x_range=(-5, 5)):
    """
    Plot elliptic curve y² = x³ + ax + b over real numbers

    Args:
        a, b: Curve parameters
        x_range: Tuple of (x_min, x_max)
    """
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)

    # Generate x values
    x = np.linspace(x_range[0], x_range[1], 1000)

    # Calculate y² = x³ + ax + b
    y_squared = x**3 + a*x + b

    # Only plot where y_squared >= 0 (real solutions exist)
    mask = y_squared >= 0
    x_valid = x[mask]
    y_pos = np.sqrt(y_squared[mask])
    y_neg = -y_pos

    # Plot both branches
    ax.plot(x_valid, y_pos, color=COLORS['primary'], linewidth=2.5,
            label=f'y² = x³ + {a}x + {b}')
    ax.plot(x_valid, y_neg, color=COLORS['primary'], linewidth=2.5)

    # Axes
    ax.axhline(y=0, color='black', linewidth=0.5, alpha=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5, alpha=0.5)

    # Grid
    ax.grid(True, alpha=0.3, linestyle='--')

    # Labels
    ax.set_xlabel('x', fontsize=12, fontweight='bold')
    ax.set_ylabel('y', fontsize=12, fontweight='bold')
    ax.set_title(f'Elliptic Curve: y² = x³ + {a}x + {b}',
                 fontsize=14, fontweight='bold', pad=20)

    ax.legend(fontsize=11, loc='upper right')
    ax.set_xlim(x_range)

    return fig, ax

def plot_ec_finite_field(a, b, p):
    """
    Plot elliptic curve over finite field F_p

    Args:
        a, b: Curve parameters
        p: Prime modulus
    """
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)

    # Find all points on the curve
    points = []
    for x in range(p):
        y_squared = (x**3 + a*x + b) % p
        for y in range(p):
            if (y**2) % p == y_squared:
                points.append((x, y))

    if points:
        xs, ys = zip(*points)
        ax.scatter(xs, ys, color=COLORS['primary'], s=100, alpha=0.7, edgecolors='white', linewidth=1.5)

    # Highlight specific points (e.g., generator)
    # Example: highlight point (2, 3)
    # ax.plot(2, 3, 'o', color=COLORS['highlight'], markersize=15, zorder=5, label='Generator G')

    # Grid
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xticks(range(p))
    ax.set_yticks(range(p))

    # Labels
    ax.set_xlabel('x', fontsize=12, fontweight='bold')
    ax.set_ylabel('y', fontsize=12, fontweight='bold')
    ax.set_title(f'Elliptic Curve over F_{p}: y² ≡ x³ + {a}x + {b} (mod {p})',
                 fontsize=14, fontweight='bold', pad=20)

    ax.set_xlim(-0.5, p-0.5)
    ax.set_ylim(-0.5, p-0.5)

    # Legend
    ax.legend(fontsize=11)

    return fig, ax

def plot_point_addition(a, b, P, Q, x_range=(-5, 5)):
    """
    Visualize point addition on elliptic curve

    Args:
        a, b: Curve parameters
        P, Q: Points to add (tuples)
        x_range: X-axis range
    """
    fig, ax = plot_ec_real_field(a, b, x_range)

    # Plot points P and Q
    ax.plot(P[0], P[1], 'o', color=COLORS['highlight'], markersize=12, zorder=5, label='Point P')
    ax.plot(Q[0], Q[1], 's', color=COLORS['secondary'], markersize=12, zorder=5, label='Point Q')

    # Calculate P + Q (simplified - you'd need actual EC addition)
    # This is just for illustration
    # slope = (Q[1] - P[1]) / (Q[0] - P[0])
    # ... actual calculation here ...

    # Draw line through P and Q
    x_line = np.linspace(x_range[0], x_range[1], 100)
    # y_line = slope * (x_line - P[0]) + P[1]
    # ax.plot(x_line, y_line, '--', color=COLORS['secondary'], linewidth=1.5, alpha=0.7, label='Line P-Q')

    # Annotate points
    ax.annotate(f'P({P[0]:.1f}, {P[1]:.1f})', P, xytext=(10, 10),
                textcoords='offset points', fontsize=10, fontweight='bold')
    ax.annotate(f'Q({Q[0]:.1f}, {Q[1]:.1f})', Q, xytext=(10, -20),
                textcoords='offset points', fontsize=10, fontweight='bold')

    ax.legend(fontsize=11, loc='upper right')

    return fig, ax

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == '__main__':
    # Example 1: Real field
    print("Generating EC over real field...")
    fig1, ax1 = plot_ec_real_field(a=-1, b=1)
    plt.tight_layout()
    plt.savefig('ch07-fig01-ec-real-field.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    plt.close()

    # Example 2: Finite field
    print("Generating EC over finite field...")
    fig2, ax2 = plot_ec_finite_field(a=2, b=3, p=17)
    plt.tight_layout()
    plt.savefig('ch07-fig02-ec-finite-field.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    plt.close()

    # Example 3: Point addition (simplified)
    print("Generating point addition visualization...")
    fig3, ax3 = plot_point_addition(a=-1, b=1, P=(0, 1), Q=(1, 1))
    plt.tight_layout()
    plt.savefig('ch07-fig03-point-addition.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    plt.close()

    print("\nAll figures generated successfully!")
