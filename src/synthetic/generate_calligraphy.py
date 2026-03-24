#!/usr/bin/env python3
import os
import random
import numpy as np
from PIL import Image, ImageDraw

def generate_calligraphy_sequence(seq_id, num_frames=40, num_views=8, size=512, base_dir="data/ICH-Synth/calligraphy"):
    """
    Generate a 4D (3D+time) synthetic sequence for Calligraphy.
    Includes 8 views per frame and ground-truth camera matrices.
    """
    seq_dir = os.path.join(base_dir, f"seq_{seq_id:03d}")
    os.makedirs(seq_dir, exist_ok=True)
    
    # Simulate a "brush stroke" (a moving line that gets thicker/thinner)
    last_pos = (random.randint(100, 400), random.randint(100, 400))
    current_stroke = [last_pos]
    
    for f in range(num_frames):
        # Update tip position (smoothly moving)
        next_pos = (
            last_pos[0] + random.randint(-15, 15),
            last_pos[1] + random.randint(-15, 15)
        )
        current_stroke.append(next_pos)
        last_pos = next_pos
            
        frame_dir = os.path.join(seq_dir, f"frame_{f:03d}")
        os.makedirs(frame_dir, exist_ok=True)
        
        # Base white paper
        base_white = (245, 245, 240)
        
        for v in range(num_views):
            # Create a view-dependent background and lighting
            img = Image.new('RGB', (size, size), color=base_white)
            draw = ImageDraw.Draw(img)
            
            # Draw the accumulated strokes (black ink)
            view_offset = int((v - num_views/2) * 8)
            for i in range(1, len(current_stroke)):
                # Get coordinates as explicit integers
                x1, y1 = current_stroke[i-1]
                x2, y2 = current_stroke[i]
                p1 = (x1 + view_offset, y1)
                p2 = (x2 + view_offset, y2)
                # Thickness varies with frame index (simulating pressure)
                width = int(5 + 10 * np.sin(f/10.0)) 
                draw.line([p1, p2], fill=(20, 20, 20), width=width)
            
            img.save(os.path.join(frame_dir, f"view_{v:02d}.png"))
            
    # Save a mock camera matrix (intrinsics/extrinsics) for NeRF compatibility
    camera_data = {
        'intrinsics': np.eye(3).tolist(),
        'extrinsics': [np.eye(4).tolist() for _ in range(num_views)]
    }
    np.save(os.path.join(seq_dir, "cameras.npy"), camera_data)

if __name__ == "__main__":
    print("Generating Calligraphy (书法) Benchmark (50 sequences)...")
    for i in range(1, 51):
        generate_calligraphy_sequence(i)
        if i % 10 == 0:
            print(f"Generated {i}/50 sequences...")
    print("Done!")
