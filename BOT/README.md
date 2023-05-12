Se desarrola un bot funciona para la aplicación Discord.

El proyecto se desarrolla en lenguaje python, con base de datos en entorno sql.

La idea principal del proyecto es realizar un bot que se conecte y funcione dentro de un servidor especifico en la aplicacion "Discord", debe reaccionar a ciertas palabras entregadas por cualquier usuario, las conecciones, lecturas de mensajes y reacciones se realizan en la carpeta "discord_listener".

Se trabajo en las siguientes reacciones:

En el contexto cumpleaños de usuarios, dentro de la carpeta "birthday_manager" se realiza manejo de datos en la base de datos, cuando "bot" reacciona a palabras como 
- !birthday 'usuario' , que nos entrega la fecha de cumpleaños de 'usuario'.
- !add-birthday 'usuario' 'fecha', que agrega 'fecha' a 'usuario'  como su cumpleaños en la base de datos.
- !greeting-birthday 'fecha', que entrega un saludo a los usuarios que cumplen años en 'fecha'.
 
 En el contexto de musica, dentro de la carpeta "search_music", se realiza conecciones y busquedas dentro de la plataforma "YouTube" cuando "bot" reacciona a palabras como
 - !seach_music 'tema', que muestra recomendaciones de la plataforma "youtube" que tienen relación con 'tema'.
 
 Para hacer funcionar el bot, se debe levantar desde "run_architecture.sh" los contenedores docker y luego hacer una conexión dentro de un servidor de "discord".
