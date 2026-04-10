Here’s a clean and expanded **README.md** for your project:

---

# 📸 Blur Detection Using OpenCV and Flask

## 📌 Overview

This project is a web-based application that detects whether an image is **blurry or clear** using computer vision techniques. It combines the power of **OpenCV** for image processing and **Flask** for building a simple and interactive web interface.

## 🚀 How It Works

The system uses the **Variance of Laplacian** method to measure image sharpness:

* The uploaded image is converted to grayscale
* The **Laplacian operator** is applied to detect edges
* The variance (spread of pixel intensity) is calculated
* If the variance is **below a threshold**, the image is classified as *blurry*
* If the variance is **above the threshold**, the image is considered *clear*

## 🌐 Features

* Upload images through a simple web interface
* Real-time blur detection
* Fast and lightweight processing
* Easy to integrate into other applications

## 🛠️ Tech Stack

* **Python**
* **OpenCV** (Image Processing)
* **Flask** (Web Framework)
* HTML/CSS (Frontend)

## 📂 Project Structure

```
blur-detection/
│── app.py
│── templates/
│   └── index.html
│── static/
│   └── uploads/
│── requirements.txt
│── README.md
```

## ▶️ How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
2. Run the Flask app:

   ```bash
   python app.py
   ```
3. Open browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

## ⚙️ Applications

* Image quality checking
* Document scanning systems
* Camera apps
* Photography tools

## ⚠️ Limitations

* Sensitive to lighting conditions
* Motion blur may affect accuracy
* Threshold tuning is required for best results

## 📌 Conclusion

This project provides a simple yet effective solution for detecting blurred images. It demonstrates how computer vision and web technologies can be combined to create practical, real-world applications.

![Gemini_Generated_Image_mazgg3mazgg3maz](https://github.com/user-attachments/assets/06c9ad5c-0268-4fd5-a4a9-e0bedb03488a)
