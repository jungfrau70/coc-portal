# Dockerfile
FROM node:16.16.0-alpine as builder

ENV PATH /app/node_modules/.bin:$PATH

WORKDIR /app
COPY app/ .

RUN yarn install \
  --prefer-offline \
  --frozen-lockfile \
  --non-interactive \
  --production=false

# RUN yarn build

# RUN rm -rf node_modules && \
#   NODE_ENV=production yarn install \
#   --prefer-offline \
#   --pure-lockfile \
#   --non-interactive \
#   --production=true

# FROM node:16.16.0-alpine

# WORKDIR /app

# COPY --from=builder /app  .

ENV HOST 0.0.0.0
EXPOSE 3000

# ENV NUXT_HOST=0.0.0.0
# ENV NUXT_PORT=3000

CMD [ "yarn", "dev" ]