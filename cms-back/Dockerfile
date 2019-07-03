FROM node:12-alpine

# Yarn install before copying in code to make use of Docker caching
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app
COPY package.json yarn.lock ./
USER node
RUN yarn install

# Copy in app code
COPY --chown=node:node . .

# Build
RUN yarn run tsc

EXPOSE 3000
CMD ["node", "./build/app.js"]
