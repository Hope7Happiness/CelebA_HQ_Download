# Building CelebA-HQ dataset (working in 2025!)

## Requirments

You should have `docker` installed. Make sure that you don't have to add `sudo` before `docker` command.

From now, work at the project root dir.

## Step 1: Download CelebA & CelebA-HQ deltas

First make dirs

```bash
mkdir ./celebA ./celebA-HQ
mkdir -p ./celebA/Anno
```

Set up your API key at the top of `zhh_down_celeba.py`. Then run

```bash
python zhh_down_celeba.py
```

**Warning** This script is written after running the code, so can't be sure if it works. But the errors should be trivial (I guess).

## Step 2: Unzip CelebA images

```bash
cat ./celebA/img_celeba.7z.0* > ./celebA/img_celeba.7z
7z x ./celebA/img_celeba.7z -o ./celebA
```

**Note**: if `7z` file is not valid, you can try to `cat` a single `7z.00x` file and check whether is a json response that indicates your web request have failed. If that's the case, you can try to download the file manually.

### Sanity check

Primary check: Check all commands in the table.

| Command | Expected output |
| --- | --- |
| `ls -1 ./celebA/img_celeba \| wc -l` | 202599 |
| `cat ./celebA/Anno/list_landmarks_celeba.txt \| wc -l` | 202601 |
| `ls celebA-HQ \| grep zip \| wc -l` | 30 |
| `cat ./celebA-HQ/image_list.txt \| wc -l` | 30001 |

**Note**: again, if `txt` file has only one or two lines, you should check whether it is a json response.

Advanced check: check whether hash value of some files are correct. Run `python testone.py`, the output should be

```
ea255cd0ffe98ca88bff23767f7a5ece7710db57
79ef1c3db2ff4c1d31c7c5bf66493a14c7a1b5cb
98039b652aec3e72e2f78039288d33feb546f08f
```

## Step 3: Run docker image

```bash
docker pull suvojit0x55aa/celeba-hq
```

If this success, then do:

```bash
bash interact.sh
```

This will make you inside the docker container. Now you should do:

```bash
cd /data/docker
bash main.sh
```

This will start the process of building CelebA-HQ dataset. This will take a long time. The dataset is downloaded at `./main_sh_out/celeba-hq/celeba-hq`, within many folders:

| Folder | Description |
| --- | --- |
| `celeba-64` | 64x64 images |
| `celeba-128` | 128x128 images |
| `celeba-256` | 256x256 images |
| `celeba-512` | 512x512 images |
| `celeba-1024` | 1024x1024 images with `.npy` files |

## Acknowledgement

Thank the wonderful project by [suvojit-0x55aa](https://github.com/suvojit-0x55aa/celebA-HQ-dataset-download). Also, the original code comes from [PGGAN](https://github.com/tkarras/progressive_growing_of_gans)