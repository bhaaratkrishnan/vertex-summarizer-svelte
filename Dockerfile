FROM node:20-slim

WORKDIR /app

COPY /package.json /app/ 

RUN npm install 

COPY . /app/

ENV PUBLIC_FUNCTION_URL=$FUNCTION_URL

EXPOSE 3000

RUN npm run build

CMD ["node","./build"]
