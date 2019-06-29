# First stage - build
FROM node:12-alpine as build

# Yarn install before copying in code to make use of Docker caching
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app
COPY package.json yarn.lock ./
USER node
RUN yarn install

# Copy in app code
COPY --chown=node:node . .

# Build
RUN yarn run quasar build -m ssr


# Second stage - production
FROM node:12-alpine

# Yarn install before copying in code to make use of Docker caching
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app
COPY --from=build /home/node/app/dist/ssr/package.json ./
USER node
RUN yarn install --production

# Copy in built application
COPY --chown=node:node --from=build /home/node/app/dist/ssr .

EXPOSE 3000
CMD ["node", "./index.js"]
