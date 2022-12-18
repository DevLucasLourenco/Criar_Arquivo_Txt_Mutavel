def arquivo_txt_mutavel(nome_arquivo, texto):

    try:            
        ########### with read
        with open(f'{nome_arquivo}.txt', 'r') as arquivo:
            texto_arquivo = arquivo.read()
        

        ############ with write
        with open(f'{nome_arquivo}.txt','w') as arquivo:
            arquivo.write(texto_arquivo)
            arquivo.write(texto)


    except:     
        ############ with write
        with open(f'{nome_arquivo}.txt','w') as arquivo:
            arquivo.write(texto)
            
            

if __name__== "__main__": 
    arquivo_txt_mutavel('teste1','testando\n')
    
    