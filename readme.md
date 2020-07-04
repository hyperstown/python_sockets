Simple Client-Server app
#
App is containing:
- Server
- Proxy (Also work as DNS)
- Client

Client is sending 36-byte message that is being encoded and sent via socket. Proxy is interpreting query and passes message to a server. Server is decoding message then passes it to designed function. After making changes in string message is encoded and sent to client.

#

### Sources:

- [YouTube socet series](https://www.youtube.com/watch?v=Lbfe3-v7yE0&list=PLQVvvaa0QuDdzLB_0JSTTcl8E8jsJLhR5&index=1)

- [Old blog](
    https://pymotw.com/2/socket/tcp.html
)

- [cpp0x](
    http://cpp0x.pl/artykuly/?id=66
)