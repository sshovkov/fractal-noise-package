import matplotlib.pyplot as plt
from fractal_noise import fractal_noise

# Generate Fractal Noise
width = 100
height = 100
scale = 0.1
octaves = [0, 1, 2, 3, 4, 5]

noise = fractal_noise(width, height, scale, octaves)

# Display Fractal Noise
plt.imshow(noise, cmap="gray")
plt.show()
