## Code2Doc

<p>
The Code2Doc is a powerful tool that harnesses the capabilities of the FLAN T5 base model combined with various fine-tuning techniques followed by a hypernetwork LoRA fusion to assist users in understanding the functionality of the code snippets by providing simple and efficient documentation for the corresponding snippets.
</p>

<!-- ![Alt text2sql](assets/ui.png) -->

## To run the application locally:

<p>

 ```
 git clone https://github.com/Chandrahas-B/Code2Doc.git
 cd Code2Doc
 ```


Models: <a href= "https://drive.google.com/drive/folders/1b5H3sI4sEN69aPcuXS3YbJGfrXhZ_F0k?usp=sharing"> Click here </a>

Tokenizers: <a href= "https://drive.google.com/drive/folders/1b5H3sI4sEN69aPcuXS3YbJGfrXhZ_F0k?usp=sharing"> Click here </a>

- Using pip:
```
pip install -r requirements.txt
python main.py
```

- Using conda:
```
conda env create -f environment.yml
python main.py
```
</p>

Note: The application runs on port 8000 by default.