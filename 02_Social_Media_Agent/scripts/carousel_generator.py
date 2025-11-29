import sys
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
# CRITICAL: Update this path to where n8n saves files
# Linux/Docker/Pinokio: "/home/node/.n8n/assets/"
# Windows: "C:/Users/YourName/n8n_assets/"
ASSET_DIR = "/home/node/.n8n/assets/"

# Canvas Settings (Instagram Portrait 4:5)
CANVAS_SIZE = (1080, 1350) 
BG_COLOR = (20, 20, 20)      # Dark Matte Grey
TEXT_COLOR = (255, 255, 255) # White

# Font Settings
# Try to put a real .ttf file in this scripts folder for best results.
# Example: "Roboto-Bold.ttf"
FONT_PATH = "arial.ttf" 
FONT_SIZE = 60

def generate_slides(input_string):
    print(f"🎨 Starting Design Engine...")
    
    # Ensure asset dir exists
    if not os.path.exists(ASSET_DIR):
        os.makedirs(ASSET_DIR)
        print(f"Created directory: {ASSET_DIR}")

    # Load Font
    try:
        # Try loading custom/system font
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except IOError:
        # Fallback to default (looks pixelated but works)
        font = ImageFont.load_default()
        print("⚠️ Warning: Custom font not found. Using default system font.")

    # Parse Input (Split by the '|||' delimiter set in n8n)
    slides = input_string.split('|||')
    
    generated_files = []

    for i, text in enumerate(slides):
        try:
            # 1. Create Blank Canvas
            img = Image.new('RGB', CANVAS_SIZE, color=BG_COLOR)
            d = ImageDraw.Draw(img)
            
            # 2. Text Wrapping Logic
            # Approx 25 chars per line for font size 60
            lines = textwrap.wrap(text, width=25) 
            
            # 3. Calculate Vertical Center
            # Get height of one line
            line_height = font.getbbox("hg")[3] + 15 
            total_text_height = len(lines) * line_height
            y_text = (CANVAS_SIZE[1] - total_text_height) / 2
            
            # 4. Draw Each Line Centered
            for line in lines:
                # Calculate horizontal center for this specific line
                line_width = font.getbbox(line)[2]
                x_text = (CANVAS_SIZE[0] - line_width) / 2
                
                d.text((x_text, y_text), line, font=font, fill=TEXT_COLOR)
                y_text += line_height
                
            # 5. Add Slide Counter (Bottom Left)
            d.text((50, 1250), f"{i+1}/{len(slides)}", font=font, fill=(100, 100, 100))

            # 6. Save File
            filename = f"insta_slide_{i+1}.jpg"
            output_path = os.path.join(ASSET_DIR, filename)
            img.save(output_path)
            generated_files.append(output_path)
            print(f"✅ Generated: {filename}")
            
        except Exception as e:
            print(f"❌ Error generating slide {i}: {e}")

    print(f"🎉 Process Complete. {len(generated_files)} slides created.")

if __name__ == "__main__":
    # n8n passes arguments as command line args
    if len(sys.argv) > 1:
        # sys.argv[1] is the argument we passed in the 'Execute Command' node
        input_data = sys.argv[1]
        generate_slides(input_data)
    else:
        print("❌ Error: No text input provided. Run this from n8n.")