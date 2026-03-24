#!/usr/bin/env python3
import sys
import os

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_paper_cutting import generate_paper_cutting_sequence
from generate_calligraphy import generate_calligraphy_sequence
from generate_shadow_puppetry import generate_shadow_puppetry_sequence

def main():
    print("="*60)
    print("ICH-Synth Benchmark Generation Pipeline")
    print("="*60)
    print("Generating 150 synthetic ICH motion sequences...")
    
    # Paper Cutting: 60 sequences
    print("\n[1/3] Generating Paper Cutting (剪纸)...")
    for i in range(1, 61):
        generate_paper_cutting_sequence(i)
        if i % 20 == 0: print(f"  Progress: {i}/60")
        
    # Calligraphy: 50 sequences
    print("\n[2/3] Generating Calligraphy (书法)...")
    for i in range(1, 51):
        generate_calligraphy_sequence(i)
        if i % 20 == 0: print(f"  Progress: {i}/50")
        
    # Shadow Puppetry: 40 sequences
    print("\n[3/3] Generating Shadow Puppetry (皮影戏)...")
    for i in range(1, 41):
        generate_shadow_puppetry_sequence(i)
        if i % 20 == 0: print(f"  Progress: {i}/40")
        
    print("\n" + "="*60)
    print("SUCCESS: ICH-Synth Benchmark Generated!")
    print(f"Data location: {os.path.abspath('data/ICH-Synth')}")
    print("="*60)

if __name__ == "__main__":
    main()
