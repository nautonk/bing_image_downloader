import sys
from bing_image_downloader import downloader

query=sys.argv[1]

if len(sys.argv) == 3:
    filter=sys.argv[2]
else:
    filter="clipart"
    
            
downloader.download(
    query,
    limit=50,
    output_dir="dataset",
    adult_filter_off=True,
    force_replace=False,
    timeout=60,
    filter=filter,
    size='large',
    verbose=True,
)

