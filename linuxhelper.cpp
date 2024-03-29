#include <signal.h>
#include <X11/Xlib.h>
#include <gdk/gdkx.h>
#include <gtk/gtk.h>

#include "include/capi/cef_app_capi.h"

static void fix_default_x11_visual(GtkWidget* widget) {
    #if GTK_CHECK_VERSION(3,15,1)
    // GTK+ > 3.15.1 uses an X11 visual optimized for GTK+'s OpenGL stuff
    // since revid dae447728d: https://github.com/GNOME/gtk/commit/dae447728d
    // However, it breaks CEF: https://github.com/cztomczak/cefcapi/issues/9
    // Let's use the default X11 visual instead of the GTK's blessed one.
    GdkScreen* screen = gdk_screen_get_default();
    GList* visuals = gdk_screen_list_visuals(screen);
    GdkX11Screen* x11_screen = GDK_X11_SCREEN(screen);
    g_return_if_fail(x11_screen != NULL);
    Visual* default_xvisual = DefaultVisual(GDK_SCREEN_XDISPLAY(x11_screen), GDK_SCREEN_XNUMBER(x11_screen));
    GList* cursor = visuals;
    while (cursor != NULL) {
        GdkVisual* visual = GDK_X11_VISUAL(cursor->data);
        if (default_xvisual->visualid == gdk_x11_visual_get_xvisual(visual)->visualid) {
            gtk_widget_set_visual(widget, visual);
            printf("gtk visual fixed\n");
            break; 
        }
        cursor = cursor->next;
    }
    g_list_free(visuals);
    #endif
}

extern "C" void FillWindowInfo(cef_window_info_t *wi, int xid, int x, int y, int width, int height)
{
#if 0
    //GtkWidget *widget = GTK_WIDGET(w);
    GtkWidget *widget = GTK_WIDGET(w);
    GdkWindow *window = gtk_widget_get_window(widget);
    Window xid = GDK_WINDOW_XID(window);
#endif
    wi->parent_window = xid;
    wi->bounds.x = x;
    wi->bounds.y = y;
    wi->bounds.width = width;
    wi->bounds.height = height;
}

extern "C" void FixGtk(void *window)
{
    GtkWidget *widget = GTK_WIDGET(window);
    fix_default_x11_visual(widget);
}

extern "C" void SetX11WindowBounds(Window xwindow, Display *xdisplay, int x, int y, int width, int height)
{
    XWindowChanges changes = {0};
    changes.x = x;
    changes.y = y;
    changes.width = width;
    changes.height = height;
    XConfigureWindow(xdisplay, xwindow, CWX | CWY | CWHeight | CWWidth, &changes);
}

extern "C" void DebugBreak()
{
    raise(SIGINT);
}
