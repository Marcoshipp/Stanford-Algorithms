import math
import random

def closest_pair(Px, Py):
    if len(Px) <= 3:
        if len(Px) == 3:
            d1 = dist(Px[0], Px[1])
            d2 = dist(Px[0], Px[2])
            d3 = dist(Px[1], Px[2])
            if d1 < d2 and d1 < d3:
                return (Px[0], Px[1])
            elif d2 < d3 and d2 < d1:
                return (Px[0], Px[2])
            else:
                return (Px[1], Px[2])
        return (Px[0], Px[1])
    else:
        half = len(Px) // 2
        x_bar = Px[half][0]
        Lx, Rx = Px[:half], Px[half:]
        Ly, Ry = [pos for pos in Py if pos[0] < x_bar], [pos for pos in Py if pos[0] >= x_bar]
        l1, l2 = closest_pair(Lx, Ly)
        r1, r2 = closest_pair(Rx, Ry)
        delta = min(dist(l1, l2), dist(r1, r2))
        split_pair = closest_split_pair(Px, Py, delta)
        if split_pair is None:
            if dist(l1, l2) > dist(r1, r2):
                return (r1, r2)
            return (l1, l2)
        else:
            s1, s2 = split_pair
            if dist(l1, l2) < dist(r1, r2) and dist(l1, l2) < dist(s1, s2):
                return (l1, l2)
            elif dist(r1, r2) < dist(l1, l2) and dist(r1, r2) < dist(s1, s2):
                return (r1, r2)
            else:
                return (s1, s2)

def closest_split_pair(Px, Py, delta):
    x_bar = Px[len(Px) // 2][0]
    Sy = [p for p in Py if (x_bar + delta > p[0] > x_bar - delta)]
    best = delta
    best_pair = None
    for i in range(len(Sy)):
        for j in range(1, 7):
            if i + j >= len(Sy):
                break
            if dist(Sy[i], Sy[i + j]) < best:
                best = dist(Sy[i], Sy[i + j])
                best_pair = (Sy[i], Sy[i + j])
    return best_pair

def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def generate_points(num_points):
    points = []
    for _ in range(num_points):
        x = random.uniform(-200, 200)  # Adjust the range as needed
        y = random.uniform(-200, 200)  # Adjust the range as needed
        points.append((x, y))
    return points

if __name__ == "__main__":
    points = generate_points(200)
    Px = sorted(points, key=lambda p: p[0])
    Py = sorted(points, key=lambda p: p[1])
    best_pair1 = closest_pair(Px, Py)
    print(f"Best pair: {best_pair1}\ndist: {dist(best_pair1[0], best_pair1[1])}")