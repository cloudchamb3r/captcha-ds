# **CAPTCHA-DS** 🧩

**CAPTCHA-DS** is a collective intelligence project aimed at building a comprehensive CAPTCHA dataset. This project relies on a community-driven effort to label, verify, and organize CAPTCHA images for use in training and testing machine learning models.

## **Project Workflow** 🚀

The dataset creation is organized into several steps, each with its own directory for processing and storing the images. Here's how you can contribute:

### **1. Working with Images (`01.working`)** 📝
   - All CAPTCHA images that need to be labeled are stored in the `01.working` directory.
   - Your task is to **rename each image file** based on the four-digit CAPTCHA text visible in the image.
   - If the CAPTCHA text is **1234**, rename the file to `1234.png`.
   - If a file with that name already exists, use the format:  
     `{captcha}.{number}.png`  
     For example, if `1234.png` already exists, the next file would be `1234.1.png`, then `1234.2.png`, and so on.
   - Once you have renamed an image, **move it** to the `02.labeled` directory for further processing.

### **2. Labeling Completed (`02.labeled`)** ✅
   - This directory contains images that have been labeled and are awaiting verification.
   - Once an image is in this directory, it will be reviewed for accuracy.

### **3. Verification (`03.verified`)** 🔍
   - Labeled images that have been verified are moved to the `03.verified` directory.
   - This is the final stage where the images are confirmed to be accurate and ready for dataset inclusion.

## **How to Contribute** 🌟

1. **Download Images**: Start by accessing the images in the `01.working` directory.
2. **Rename Images**: Follow the naming guidelines based on the CAPTCHA text you see.
3. **Avoid Duplicates**: If a file with the same CAPTCHA text already exists, use the `{captcha}.{number}.png` format.
4. **Move Labeled Images**: Transfer the renamed file to the `02.labeled` directory once you're done.
5. **Verification**: You can also help verify the accuracy of labeled images in the `02.labeled` directory and move them to `03.verified` if correct.

## **Directory Structure** 📂

```
CAPTCHA-DS/
├── 01.working/     # Images awaiting labeling
├── 02.labeled/     # Labeled images pending verification
└── 03.verified/    # Verified and final images
```

## **Conventions** ✏️

- All CAPTCHA labels should be **4-digit numbers**.
- Use the `{captcha}.png` format for file names.
- Use the `{captcha}.{number}.png` format if there's a name conflict.

## **Contact & Contribution** 🤝

Feel free to reach out with suggestions or questions. Contributions are welcome! To contribute:
- Fork the repository
- Make your changes
- Submit a pull request

Help us create a valuable resource for CAPTCHA analysis and research!
