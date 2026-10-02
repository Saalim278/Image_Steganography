📌 Overview
Image Steganography is a technique of concealing information within digital images without visibly altering their appearance.
This project uses the Least Significant Bit (LSB) technique to embed secret messages into images. Built with Python and Tkinter, it provides an interactive desktop interface for encoding and decoding messages without requiring command-line operations.

✨ Features

* Hide Messages: Embed secret text messages into images using LSB steganography.
* Extract Messages: Retrieve hidden messages from encoded images.
* Graphical User Interface: Simple desktop interface developed using Tkinter.
* Image Selection: Select images from the local system using a file dialog.
* Save Encoded Images: Save images containing hidden messages.
* Error Handling: Display alerts and error messages using Tkinter message boxes.
* Local Processing: Perform encoding and decoding directly on the local system.

🛠️ Tech Stack

| Technology   | Purpose                                 |
| ------------ | --------------------------------------- |
| Python       | Core application logic                  |
| Tkinter      | Graphical user interface                |
| Pillow (PIL) | Image handling and processing           |
| Stegano      | LSB-based message encoding and decoding |
| `filedialog` | Image selection and saving              |
| `messagebox` | Alerts, errors and user notifications   |

⚙️ How It Works

The application uses the Least Significant Bit (LSB) steganography technique through the `stegano` library.

🔹 Encoding

1. Select an image from the local system using `filedialog`.
2. Enter the secret text message.
3. Use `stegano.lsb` to hide the message within the image.
4. Save the encoded image to the desired location.

🔹 Decoding

1. Select the encoded image.
2. Use `stegano.lsb` to extract the concealed message.
3. Display the extracted message in the application.
4. Show relevant notifications using `messagebox`.

📂 Project Structure

```text
Image_Steganography/
│
├── main.py
├── README.md
└── requirements.txt
```

*Adjust the structure to match the actual files in your repository.*

🚀 Installation & Setup

Prerequisites

* Python 3.x
* pip

1. Clone the Repository

```bash
git clone https://github.com/Saalim278/Image_Steganography.git
```

2. Navigate to the Project Directory

```bash
cd Image_Steganography
```

3. Install Dependencies

```bash
pip install pillow stegano
```

Tkinter is generally included with standard Python installations, although some Linux distributions require a separate package.

4. Run the Application

```bash
python main.py
```

Replace `main.py` with the actual entry-point filename if necessary.

💻 Technologies & Libraries

* **Tkinter**: Used to develop the graphical interface and handle user interactions.
* **Pillow (PIL):** Provides image-handling and processing capabilities.
* **Stegano (`lsb`):** Provides functionality to encode and decode hidden messages using LSB steganography.
* **Filedialog:** Enables users to browse, select and save image files.
* **Messagebox:** Provides user feedback through information, warning and error dialogs.

🎯 Learning Outcomes

* Developed a desktop application using Python and Tkinter.
* Applied LSB-based image steganography using the Stegano library.
* Integrated third-party Python libraries into an application.
* Implemented file selection and image-saving workflows.
* Practiced event-driven programming and GUI-based user interaction.
* Applied exception handling and user feedback mechanisms.

⚠️ Limitations

* The amount of text that can be hidden depends on the image's capacity.
* Image resizing or lossy compression may destroy the embedded message.
* LSB steganography does not encrypt the hidden message.
* The presence of concealed data may be detectable using steganalysis techniques.

🔮 Future Enhancements

* Add password-based encryption to protect hidden messages.
* Support more image formats.
* Display the maximum message capacity before encoding.
* Improve validation and error handling.
* Enhance the graphical interface for a better user experience.
