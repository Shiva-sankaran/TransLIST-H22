/home/vp.shivasan/word_segmentation/working_dir/TransLIST/load_data.py 
    train,val,test paths

/home/vp.shivasan/word_segmentation/working_dir/TransLIST/embedding_gen.py
    create embeddings for H22



cd TransLIST-H22
conda env create -f tlat0.yml
conda activate tlat0
bash requirements.sh /home/vp.shivasan/miniconda3/envs [PATH to your conda environments] (e.g. ~/anaconda3/envs)
Run embedding_gen.py
Run ngram_lat_gen.py
Replace  FastNLP dataset.py with /home/vp.shivasan/word_segmentation/TransLIST-H22/fastNLP-H22_files/dataset.py

find . -maxdepth 1 -name "*.lat" -print0 | xargs -0 rm