#!/usr/bin/env python3
"""Simple Voronoi diagram via pixel assignment."""
import sys, math

def voronoi_ascii(sites, w=60, h=30):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    grid = []
    for y in range(h):
        row = []
        for x in range(w):
            best_d, best_s = float('inf'), 0
            for i, (sx, sy) in enumerate(sites):
                d = math.sqrt((x-sx)**2 + (y-sy)**2)
                if d < best_d: best_d, best_s = d, i
            row.append(symbols[best_s % len(symbols)])
        grid.append("".join(row))
    return grid

def main():
    sites = [(10,5),(30,15),(50,10),(20,25),(45,22)]
    grid = voronoi_ascii(sites)
    for row in grid: print(row)
    print(f"Sites: {sites}")

if __name__ == "__main__": main()
