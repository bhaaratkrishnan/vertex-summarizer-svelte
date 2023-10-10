# Copyright 2022 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     https://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


FROM node:20-slim

WORKDIR /app

COPY /package.json /app/ 

RUN npm install 

COPY . /app/

ENV PUBLIC_FUNCTION_URL=$FUNCTION_URL

EXPOSE 3000

RUN npm run build

CMD ["node","./build"]
