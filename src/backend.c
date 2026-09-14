#include "ataristudio/backend.h"

static const AtariStudioBackendDescriptor descriptor = {
    ATARISTUDIO_RETROSTUDIO_TARGET_API_VERSION,
    "ataristudio",
    "AtariStudio Atari Backend",
    "0.0.0-m0"
};

const AtariStudioBackendDescriptor *ataristudio_describe_backend(void)
{
    return &descriptor;
}
