WORKDIR="$( cd "$(dirname "$0")" ; pwd -P )"
echo $WORKDIR

# Download CelebA unaligned images
# python $WORKDIR/download_celebA.py $1

# Download CelebA-HQ deltas
# python $WORKDIR/download_celebA_HQ.py $1

# Extract CelebA images
# cat $1/celebA/img_celeba.7z.0* > $1/celebA/img_celeba.7z
# 7z x $1/celebA/img_celeba.7z -o$1/celebA

# Create CelebA-HQ images
python $WORKDIR/dataset_tool.py \
        create_celebahq \
        /data/idk \
        /data/celebA \
        /data/celebA-HQ