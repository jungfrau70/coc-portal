# Choose the Image which has Node installed already
FROM node:16.17.1-alpine as build-stage

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY app/package*.json ./
COPY app/yarn.lock ./

# install project dependencies
# RUN yarn install
RUN yarn install \
  --prefer-offline \
  --frozen-lockfile \
  --non-interactive \
  --production=true

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY app/. .

# build app for production with minification
RUN yarn build

# EXPOSE 3000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000
EXPOSE 3000

CMD [ "yarn", "start" ]

# production stage
# FROM nginx:stable-alpine as production-stage
# COPY --from=build-stage /app/.nuxt/dist /usr/share/nginx/html
# EXPOSE 3000
# CMD ["nginx", "-g", "daemon off;"]