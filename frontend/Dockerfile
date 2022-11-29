# se servirá una página elaborada con vuejs para registrar 
# la entrega del servicio de alimentación

# ---- multistage build
# https://docs.docker.com/develop/develop-images/multistage-build/

# ---------- BUILD STAGE -----------
# seleccionando una imagen que contenga node
FROM node:16.16.0 as build-stage

# se selecciona el directorio de trabajo en el contenedor
WORKDIR /home/usr/product/

#---------- cache de las dependencias instaladas
# se copia los archivos de dependencia
COPY ./product/package.json ./
# se instalan las dependencias
RUN npm install
# ---------------- 

# se copian los demas archivos
COPY ./product ./

# se compila
RUN npm run build
# ----------- END BUILD STAGE --------------

# -------------- PRODUCTION STAGE ---------------
# nginx production server
# https://cli.vuejs.org/guide/deployment.html#docker-nginx
FROM nginx as production-stage
RUN mkdir -p /home/usr/app
# copying files from build stage container
COPY --from=build-stage /home/usr/product/dist /home/usr/app
# copying nginx config file
COPY nginx.conf /etc/nginx/nginx.conf
# ----------- END PRODUCTION STAGE ---------------

# Then the console
# >> docker build -t selobu/casino .
# >> docker run -p 80:80 selobu/casino
# otherwise check docker-compose