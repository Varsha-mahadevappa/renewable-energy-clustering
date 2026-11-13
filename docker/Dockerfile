
FROM eclipse-temurin:17-jre-jammy

ARG HBASE_VERSION=2.6.7

RUN apt-get update && \
    apt-get install -y curl procps && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fL \
    "https://downloads.apache.org/hbase/${HBASE_VERSION}/hbase-${HBASE_VERSION}-bin.tar.gz" \
    -o /tmp/hbase.tar.gz && \
    tar -xzf /tmp/hbase.tar.gz -C /opt && \
    mv /opt/hbase-${HBASE_VERSION} /opt/hbase && \
    rm /tmp/hbase.tar.gz

ENV JAVA_HOME=/opt/java/openjdk
ENV HBASE_HOME=/opt/hbase
ENV PATH="${HBASE_HOME}/bin:${PATH}"

COPY docker/hbase-site.xml /opt/hbase/conf/hbase-site.xml

RUN mkdir -p /data/hbase /data/zookeeper

EXPOSE 16000 16010 16020 9090

CMD ["bash", "-c", "start-hbase.sh && hbase thrift start -p 9090"]
