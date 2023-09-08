FROM node:20-slim

WORKDIR /app

COPY /package.json /app/ 

RUN npm install 

COPY . /app/

ENV PUBLIC_FUNCTION_URL=https://us-central1-cv3-serverless-web-apis.cloudfunctions.net/vertex-ai-test

EXPOSE 3000

RUN npm run build

CMD ["node","./build/index.js"]
