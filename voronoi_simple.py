#!/usr/bin/env python3
"""Simple Voronoi diagram (brute force). Zero dependencies."""
import math

def nearest_site(point, sites):
    best = None; best_d = float("inf")
    for i, s in enumerate(sites):
        d = math.hypot(point[0]-s[0], point[1]-s[1])
        if d < best_d: best_d = d; best = i
    return best, best_d

def voronoi_grid(sites, width, height, resolution=1):
    grid = []
    for y in range(0, height, resolution):
        row = []
        for x in range(0, width, resolution):
            idx, _ = nearest_site((x, y), sites)
            row.append(idx)
        grid.append(row)
    return grid

def voronoi_boundaries(sites, width, height, resolution=1):
    grid = voronoi_grid(sites, width, height, resolution)
    boundaries = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            v = grid[y][x]
            for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                ny, nx = y+dy, x+dx
                if 0<=ny<len(grid) and 0<=nx<len(grid[0]) and grid[ny][nx] != v:
                    boundaries.append((x*resolution, y*resolution))
                    break
    return boundaries

def lloyd_relaxation(sites, width, height, iterations=1):
    import copy
    sites = [list(s) for s in sites]
    for _ in range(iterations):
        grid = voronoi_grid(sites, width, height)
        sums = [[0,0,0] for _ in sites]  # x_sum, y_sum, count
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                idx = grid[y][x]
                sums[idx][0] += x; sums[idx][1] += y; sums[idx][2] += 1
        for i in range(len(sites)):
            if sums[i][2] > 0:
                sites[i] = [sums[i][0]/sums[i][2], sums[i][1]/sums[i][2]]
    return [tuple(s) for s in sites]

if __name__ == "__main__":
    sites = [(10,10),(30,30),(50,10)]
    grid = voronoi_grid(sites, 60, 40, 5)
    for row in grid: print("".join(str(c) for c in row))
