import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from google.colab import files

# ✅ Use your uploaded image
logo_path = "file_000000009808620a9a88dcc124f4a0cd.png"
logo = Image.open(logo_path).convert("RGBA")

frames = []
fig, ax = plt.subplots(figsize=(5, 5))
plt.axis("off")

for i in range(60):
    ax.clear()
    ax.axis("off")
    ax.set_facecolor("black")

    # Logo drop
    if i < 20:
        y_offset = 1 - i * 0.05
    else:
        y_offset = 0
    ax.imshow(logo, extent=[-0.5, 0.5, y_offset-0.5, y_offset+0.5])

    # Blast effect
    if 20 <= i < 30:
        for _ in range(10):
            x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
            ax.text(x, y, "$", color="lime", fontsize=15, ha="center", va="center", alpha=1-(i-20)/10)

    # Text animation
    text = "UndrCash"
    if i >= 30:
        letters_to_show = (i - 30) // 5 + 1
        ax.text(0, -0.8, text[:letters_to_show], color="white",
                fontsize=22, ha="center", va="center", fontweight="bold")

    # Save frame
    fig.canvas.draw()
    frame = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    frame = frame.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    frames.append(Image.fromarray(frame))

plt.close()

# Save as GIF
frames[0].save("undrcash.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)

# ✅ Download from Colab
files.download("undrcash.gif")
