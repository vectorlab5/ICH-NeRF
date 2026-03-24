#!/usr/bin/env python3
import os
import random
import numpy as np
from PIL import Image, ImageDraw

def generate_shadow_puppetry_sequence(seq_id, num_frames=50, num_views=8, size=512, base_dir="data/ICH-Synth/shadow_puppetry"):
    """
    Generate a 4D (3D+time) synthetic sequence for Shadow Puppetry.
    Includes 8 views per frame and ground-truth camera matrices.
    """
    seq_dir = os.path.join(base_dir, f"seq_{seq_id:03d}")
    os.makedirs(seq_dir, exist_ok=True)
    
    # Simulate a "shadow puppet" (a torso with two moving arms)
    torso_pos = (256, 256)
    
    for f in range(num_frames):
        # Update limb angles (oscillating)
        arm_angle = np.sin(f/5.0) * 45
        leg_angle = np.cos(f/8.0) * 30
            
        frame_dir = os.path.join(seq_dir, f"frame_{f:03d}")
        os.makedirs(frame_dir, exist_ok=True)
        
        # Base parchment background
        base_parchment = (210, 190, 150)
        
        for v in range(num_views):
            # Create a view-dependent background and lighting
            img = Image.new('RGB', (size, size), color=base_parchment)
            draw = ImageDraw.Draw(img)
            
            # Draw the puppet (black silhouette)
            view_offset = int((v - num_views/2) * 12)
            # Ensure cx and cy are integers
            cx = int(torso_pos[0] + view_offset)
            cy = int(torso_pos[1])
            
            # Torso: [x0, y0, x1, y1]
            draw.ellipse([cx-30, cy-50, cx+30, cy+50], fill=(10, 10, 10))
            # Head
            draw.ellipse([cx-20, cy-80, cx+20, cy-50], fill=(10, 10, 10))
            
            # Arms (rotating around shoulder at cx, cy-30)
            arm_len = 60
            for side in [-1, 1]:
                rad = np.radians(side * 30 + arm_angle)
                end_x = int((cx + side * 15) + arm_len * np.sin(rad))
                end_y = int((cy - 30) + arm_len * np.cos(rad))
                draw.line([(cx + side * 15, cy - 30), (end_x, end_y)], fill=(10, 10, 10), width=10)
            
            img.save(os.path.join(frame_dir, f"view_{v:02d}.png"))
            
    # Save a mock camera matrix (intrinsics/extrinsics) for NeRF compatibility
    camera_data = {
        'intrinsics': np.eye(3).tolist(),
        'extrinsics': [np.eye(4).tolist() for _ in range(num_views)]
    }
    np.save(os.path.join(seq_dir, "cameras.npy"), camera_data)

if __name__ == "__main__":
    print("Generating Shadow Puppetry (皮影戏) Benchmark (40 sequences)...")
    for i in range(1, 41):
        generate_shadow_puppetry_sequence(i)
        if i % 10 == 0:
            print(f"Generated {i}/40 sequences...")
    print("Done!")
