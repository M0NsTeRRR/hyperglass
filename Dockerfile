FROM python:3.12.3-alpine as base
LABEL org.opencontainers.image.title=hyperglass
LABEL org.opencontainers.image.description="hyperglass is an open source network looking glass"
LABEL org.opencontainers.image.authors="Matt Love <matt@stunninglyclear.com>"
LABEL org.opencontainers.image.url=https://github.com/thatmattlove/hyperglass
LABEL org.opencontainers.image.licenses=BSD-3-Clause
WORKDIR /opt/hyperglass
ENV HYPERGLASS_APP_PATH=/etc/hyperglass
ENV HYPERGLASS_HOST=0.0.0.0
ENV HYPERGLASS_PORT=8001
ENV HYPERGLASS_DEBUG=false
ENV HYPERGLASS_DEV_MODE=false
ENV HYPERGLASS_REDIS_HOST=redis
ENV HYPEGLASS_DISABLE_UI=true
ENV HYPERGLASS_CONTAINER=true
COPY . .

FROM base as ui
WORKDIR /opt/hyperglass/hyperglass/ui
RUN apk add build-base pkgconfig cairo-dev nodejs npm
RUN npm install -g pnpm
RUN pnpm install -P

FROM ui as hyperglass
WORKDIR /opt/hyperglass
RUN pip3 install -e .

EXPOSE ${HYPERGLASS_PORT}
CMD ["python3", "-m", "hyperglass.console", "start"]
