// CEF C API example
// Project website: https://github.com/cztomczak/cefcapi

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "include/capi/cef_base_capi.h"
#include "include/capi/cef_app_capi.h"
#include "include/capi/cef_client_capi.h"
#include "include/capi/cef_life_span_handler_capi.h"

#include "include/cef_version.h"

#include "icef_base.h"
#include "icef_app.h"
#include "icef_client.h"
#include "icef_life_span_handler.h"

// Globals
cef_life_span_handler_t g_life_span_handler;

void cef_str(char *s, cef_string_t *t)
{
    cef_string_utf8_to_utf16(s, strlen(s), t);
}

int main(int argc, char** argv) {
    cef_main_args_t main_args;
    cef_app_t app;
    cef_settings_t settings;
    cef_window_info_t window_info;
    cef_string_t cef_url;
    char url[] = "http://html5test.com/";
    cef_client_t client;
    cef_browser_settings_t browser_settings;
    int code;

#define ZERO(s) memset(&s, 0, sizeof(s))
    ZERO(g_life_span_handler);
    ZERO(main_args);
    ZERO(app);
    ZERO(settings);
    ZERO(window_info);
    ZERO(cef_url);
    ZERO(client);
    ZERO(browser_settings);

    // This executable is called many times, because it
    // is also used for subprocesses. Let's print args
    // so we can differentiate between main process and
    // subprocesses. If one of the first args is for
    // example "--type=renderer" then it means that
    // this is a Renderer process. There may be more
    // subprocesses like GPU (--type=gpu-process) and
    // others. On Linux there are also special Zygote
    // processes.
    printf("\nProcess args: ");
    if (argc == 1) {
        printf("none (Main process)");
    } else {
        for (int i = 1; i < argc; i++) {
            if (strlen(argv[i]) > 128)
                printf("... ");
            else
                printf("%s ", argv[i]);
        }
    }
    printf("\n\n");

    // CEF version
    if (argc == 0) {
        printf("CEF version: %s\n", CEF_VERSION);
    }

    // Main args
    main_args.instance = GetModuleHandle(NULL);

    // Cef app
    initialize_cef_app(&app);
    
    // Execute subprocesses. It is also possible to have
    // a separate executable for subprocesses by setting
    // cef_settings_t.browser_subprocess_path. In such
    // case cef_execute_process should not be called here.
    printf("cef_execute_process, argc=%d\n", argc);
    code = cef_execute_process(&main_args, &app, NULL);
    if (code >= 0) {
        _exit(code);
    }
    
    // Application settings. It is mandatory to set the
    // "size" member.
    settings.size = sizeof(cef_settings_t);
    settings.log_severity = LOGSEVERITY_WARNING; // Show only warnings/errors
    settings.no_sandbox = 1;
    cef_str("W:\\trisoft\\cefct\\bin\\cefclient.exe", &settings.browser_subprocess_path);
    cef_str("w:\\trisoft\\cefct\\bin-cefdata\\root", &settings.root_cache_path);
    cef_str("w:\\trisoft\\cefct\\bin-cefdata\\root\\cache", &settings.cache_path);
    cef_str("w:\\trisoft\\cefct\\bin-cefdata\\user-data", &settings.user_data_path);
    cef_str("w:\\trisoft\\cefct\\bin-cefdata\\cef.log", &settings.log_file);

    // Initialize CEF
    printf("cef_initialize\n");
    cef_initialize(&main_args, &settings, &app, NULL);

    // Window info
    cef_str("cef window", &window_info.window_name);
    window_info.style = WS_OVERLAPPEDWINDOW | WS_CLIPCHILDREN \
            | WS_CLIPSIBLINGS | WS_VISIBLE;
    window_info.parent_window = NULL;
    window_info.bounds.x = CW_USEDEFAULT;
    window_info.bounds.y = CW_USEDEFAULT;
    window_info.bounds.width = CW_USEDEFAULT;
    window_info.bounds.height = CW_USEDEFAULT;

    // Initial url
    cef_str(url, &cef_url);

    // Browser settings. It is mandatory to set the
    // "size" member.
    browser_settings.size = sizeof(cef_browser_settings_t);
    
    // Client handlers
    initialize_cef_client(&client);
    initialize_cef_life_span_handler(&g_life_span_handler);

    // Create browser asynchronously. There is also a
    // synchronous version of this function available.
    printf("cef_browser_host_create_browser\n");
    cef_browser_t *browser = cef_browser_host_create_browser_sync(
        &window_info,
        &client,
        &cef_url,
        &browser_settings,
        NULL,
        NULL
    );

    // Message loop. There is also cef_do_message_loop_work()
    // that allow for integrating with existing message loops.
    // On Windows for best performance you should set
    // cef_settings_t.multi_threaded_message_loop to true.
    // Note however that when you do that CEF UI thread is no
    // more application main thread and using CEF API is more
    // difficult and require using functions like cef_post_task
    // for running tasks on CEF UI thread.
    printf("cef_run_message_loop\n");
    cef_run_message_loop();

    printf("release browser\n");
    browser->base.release(&browser->base);
#if 0
    cef_request_context_t *ctx = cef_request_context_get_global_context();
    ctx->base.base.add_ref(&ctx->base.base);
    ctx->base.base.release(&ctx->base.base);
#endif

    // Shutdown CEF
    printf("cef_shutdown\n");
    cef_shutdown();

    return 0;
}
