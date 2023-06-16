for filename in /tmp/data/*.ttl
do
    graph=$(basename "$filename" .ttl) \
    && $TDBLOADER --graph=http://ldf.fi/ulan/$graph $filename || exit 1
done \
&& $TEXTINDEXER \
&& $TDBSTATS --graph urn:x-arq:UnionGraph > /tmp/stats.opt \
&& mv /tmp/stats.opt /fuseki-base/databases/tdb/
