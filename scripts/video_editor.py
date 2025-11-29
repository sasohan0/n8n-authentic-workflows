import os
import glob
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
# CRITICAL: This path must match where n8n saves the files.
# Windows Example: "C:/Users/YourName/n8n_assets/"
# Linux/Docker Example: "/home/node/.n8n/assets/"
ASSET_DIR = "/home/node/.n8n/assets/"
OUTPUT_FILENAME = "final_video.mp4"

def create_video():
    print(f"🎬 Starting Video Render in: {ASSET_DIR}")
    
    # 1. Find all audio files and sort them by index (audio_0, audio_1...)
    audio_files = sorted(glob.glob(os.path.join(ASSET_DIR, "audio_*.mp3")), key=lambda x: int(x.split('_')[-1].split('.')[0]))
    
    clips = []

    if not audio_files:
        print("❌ No audio files found. Run the n8n workflow first.")
        return

    # 2. Iterate through assets and build clips
    for audio_path in audio_files:
        # Extract index to find matching image
        filename = os.path.basename(audio_path)
        index = filename.split('_')[-1].split('.')[0]
        
        img_path = os.path.join(ASSET_DIR, f"image_{index}.jpg")
        
        if os.path.exists(img_path):
            try:
                # Load Audio
                audio_clip = AudioFileClip(audio_path)
                
                # Load Image & Set Duration to match Audio
                img_clip = ImageClip(img_path).set_duration(audio_clip.duration)
                img_clip = img_clip.set_audio(audio_clip)
                
                # Resize to 1080p (Vertical 1080x1920 or Landscape 1920x1080)
                # This ensures all images are the same size so ffmpeg doesn't crash
                img_clip = img_clip.resize(height=1080)
                # If you want 16:9 crop, you would add .crop() here
                
                clips.append(img_clip)
                print(f"✅ Scene {index} processed.")
            except Exception as e:
                print(f"⚠️ Error processing scene {index}: {e}")
        else:
            print(f"⚠️ Missing image for audio index {index}. Skipping.")

    # 3. Concatenate and Render
    if clips:
        print("rendering final video... (This may take a minute)")
        final_video = concatenate_videoclips(clips, method="compose")
        output_path = os.path.join(ASSET_DIR, OUTPUT_FILENAME)
        
        # Write file (fps=24 is standard for cinematic look)
        final_video.write_videofile(output_path, fps=24, codec='libx264', audio_codec='aac')
        print(f"🎉 SUCCESS! Video saved to: {output_path}")
    else:
        print("❌ No valid clips created.")

if __name__ == "__main__":
    create_video()