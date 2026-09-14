#include <stdio.h>
#include <string.h>
#include "ataristudio/backend.h"

int main(void)
{
    const AtariStudioBackendDescriptor *d = ataristudio_describe_backend();

    if (!d) return 1;
    if (d->api_version != ATARISTUDIO_RETROSTUDIO_TARGET_API_VERSION) return 2;
    if (strcmp(d->id, "ataristudio") != 0) return 3;
    if (strcmp(d->backend_version, "0.0.0-m0") != 0) return 4;

    puts("PASS: AtariStudio backend descriptor");
    return 0;
}
