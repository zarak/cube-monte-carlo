import random

# Each cube is represented as a list of six elements,
# where each element is 1 if the face is painted and 0 otherwise.
center_cube = [0, 0, 0, 0, 0, 0]
face_cubes = [[1, 0, 0, 0, 0, 0] for _ in range(6)]
edge_cubes = [[1, 1, 0, 0, 0, 0] for _ in range(12)]
corner_cubes = [[1, 1, 1, 0, 0, 0] for _ in range(8)]
all_cubes = [center_cube] + face_cubes + edge_cubes + corner_cubes

def run(N=1_000_000):
    count = 0  # times that face pointing down is painted given that the other five faces are not painted
    total = 0  # total number of times the other five faces are not painted
    for _ in range(N):
        cube = random.choice(all_cubes)
        
        random.shuffle(cube)
        down_face = cube[0]
        other_faces = cube[1:]
        
        # Check if the other five faces are not painted
        if sum(other_faces) == 0:
            total += 1
            if down_face == 1:
                count += 1

    return count / total

if __name__ == "__main__":
    prob = run()
    print(prob)
