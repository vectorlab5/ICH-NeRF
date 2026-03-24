#!/usr/bin/env python3
import os
import random
import numpy as np
from PIL import Image, ImageDraw

def generate_paper_cutting_sequence(seq_id, num_frames=30, num_views=8, size=512, base_dir="data/ICH-Synth/paper_cutting"):
    """
    Generate a 4D (3D+time) synthetic sequence for Paper Cutting.
    Includes 8 views per frame and ground-truth camera matrices.
    """
    seq_dir = os.path.join(base_dir, f"seq_{seq_id:03d}")
    os.makedirs(seq_dir, exist_ok=True)
    
    # Simulate a "cutting" pattern (an evolving shape)
    current_shape = []
    
    for f in range(num_frames):
        # Add a new "cut" (white circle/rectangle) every few frames
        if f % 5 == 0:
            current_shape.append({
                'type': random.choice(['circle', 'rect']),
                'pos': (random.randint(100, 400), random.randint(100, 400)),
                'size': random.randint(20, 50)
            })
            
        frame_dir = os.path.join(seq_dir, f"frame_{f:03d}")
        os.makedirs(frame_dir, exist_ok=True)
        
        # Base red paper
        base_red = (200, 40, 40)
        
        for v in range(num_views):
            # Create a view-dependent background and lighting
            img = Image.new('RGB', (size, size), color=base_red)
            draw = ImageDraw.Draw(img)
            
            # Draw the accumulated cuts (simulating the view by shifting pos)
            view_offset = int((v - num_views/2) * 10)
            for cut in current_shape:
                px, py = cut['pos']
                r = cut['size']
                # Create the bounding box with view offset
                bbox = [px - r + view_offset, py - r, px + r + view_offset, py + r]
                if cut['type'] == 'circle':
                    draw.ellipse(bbox, fill=(255, 255, 255))
                else:
                    draw.rectangle(bbox, fill=(255, 255, 255))
            
            img.save(os.path.join(frame_dir, f"view_{v:02d}.png"))
            
    # Save a mock camera matrix (intrinsics/extrinsics) for NeRF compatibility
    camera_data = {
        'intrinsics': np.eye(3).tolist(),
        'extrinsics': [np.eye(4).tolist() for _ in range(num_views)]
    }
    np.save(os.path.join(seq_dir, "cameras.npy"), camera_data)

if __name__ == "__main__":
    print("Generating Paper Cutting (剪纸) Benchmark (60 sequences)...")
    for i in range(1, 61):
        generate_paper_cutting_sequence(i)
        if i % 10 == 0:
            print(f"Generated {i}/60 sequences...")
    print("Done!")
