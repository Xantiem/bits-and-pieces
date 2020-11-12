#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h> /* close() */
#include <sys/socket.h>
#include <netdb.h>

int main(void)
{
    int sock;
    char host[] = "icecast.funradio.fr";
    char port[] = "80";
    struct addrinfo hints, *res;
    char message[] = "GET /fun-1-44-128 HTTP/1.1\r\nHost: icecast.funradio.fr\r\n\n\n";


    char buf[1024];
    int bytes_read;
    int status;

    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;

    status = getaddrinfo(host, port, &hints, &res);
    sock = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
    status = connect(sock, res->ai_addr, res->ai_addrlen);

    freeaddrinfo(res);
    send(sock, message, strlen(message), 0);

    while (bytes_read > 0) {
        bytes_read = recv(sock, buf, 1024, 0);
        printf("%s", buf);
    }

    close(sock);

    return 0;
}
