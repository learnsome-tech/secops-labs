# m05l01-03 · Acquire an image and hash it in the same pass

**Lesson:** [Forensics Principles, Custody & Imaging](https://learnsome.tech/learn/secops-course/m05l01) (lesson 5.1, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can decide what to collect first, acquire a disk image whose hashes prove it is unchanged, and keep a chain of custody with no gaps.

In the lesson: Now the acquisition. On a real case the source is the suspect drive attached through a hardware write blocker, a device that passes reads through and refuses writes. Here a helper builds a one mebibyte file to stand in for that drive. The program reads it in blocks of sixty four kibibytes. Every block feeds two running hashes, M D five and S H A two fifty six, and each block gets its own S H A two fifty six as well; those piecewise hashes pay off in a moment. Then it writes the block to the image. Hashing during the copy means the hash describes exactly what was read from the source. When the copy is done we read the image back from disk and hash it again. The output is what goes into your notes: the byte count, both hashes, and confirmation that the image on disk matches what came off the drive.

## Files

- [`starter/image.py`](starter/image.py): the listing from the lesson
- [`starter/make_disk.py`](starter/make_disk.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-03/starter`
2. Read `image.py` the way the lesson builds it:
   - Lines 1–4: a helper builds a one mebibyte file
   - Lines 5–9: reads it in blocks of sixty four kibibytes
   - Lines 10–14: Then it writes the block to the image
   - Lines 15–22: read the image back from disk and hash it again
3. Notes from the lesson:
   - Line 12: piecewise hashes: one per block, kept beside the image
4. Run it: `python3 image.py`.
5. Check it from the repository root: `./check m05l01-03`.

## Expected output

```text
bytes acquired: 1048576 in 16 blocks
md5    97db13b125aac2e5ba659f1adea1a9bf
sha256 36d94d69f8a28cc1972bb5336f12f135a27aa8e3c0341fa8992f86a5dda4e05b
image re-hash matches acquisition: True
```

## How to check

`./check m05l01-03` copies `starter/` into a scratch directory and runs `python3 image.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
