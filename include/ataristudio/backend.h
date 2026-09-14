#ifndef ATARISTUDIO_BACKEND_H
#define ATARISTUDIO_BACKEND_H

#ifdef __cplusplus
extern "C" {
#endif

#define ATARISTUDIO_RETROSTUDIO_TARGET_API_VERSION 1u

typedef struct AtariStudioBackendDescriptor {
    unsigned int api_version;
    const char *id;
    const char *display_name;
    const char *backend_version;
} AtariStudioBackendDescriptor;

const AtariStudioBackendDescriptor *ataristudio_describe_backend(void);

#ifdef __cplusplus
}
#endif

#endif
