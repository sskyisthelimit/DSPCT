from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageFilter
from pathlib import Path

def process_image(path):
    img = Image.open(path)
    img = img.resize((1024, 1024)).convert("L").filter(ImageFilter.DETAIL)
    out_dir = Path("data/images/out")
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / path.name
    img.save(out)
    return out

def main():
    files = list(Path("data/images").glob("*.jpg"))
    if not files:
        print("No .jpg files found in ./images")
        return

    with ProcessPoolExecutor(max_workers=2) as ex:
        for out_path in ex.map(process_image, files):
            print("saved", out_path)

if __name__ == "__main__":
    main()
