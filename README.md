# REPO Privado :ghost: :ghost: :ghost: 

# Comandos
    # DESCARGAR ZIP
    >>>   curl -L -o master.zip http://github.com/pl4gue/master
    # DESCARGAR REPO
    >>>   git clone git@github.com:pl4gue/private.git
    >>>   git add .  #(en ./private )
    >>>   git commit -m "Comentario"
    >>>   git push   
    >>> 
    >>>   git reset --hard
    >>>   git pull
  
# Entorno
    # Clave Pública
    >>>   //Crear clave
    >>>   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
                >>>   enter
                >>>   pass/pass
    >>>   //Iniciar agent segundo plano
    >>>   eval "$(ssh-agent -s)"
    >>>   //Añadir tu clave al ssh-Agent
    >>>   ssh-add ~/.ssh/id_rsa
    >>>   //Copiar en portapapeles la clave publica (~/.ssh/id_rsa.pub)
    >>>   //Dentro de GitHub :  Settings >> SSH and GPG >> Add New
    >>>   //Probar conexion
    >>>   ssh -T git@github.com
    
      
    
![image](command.png)
