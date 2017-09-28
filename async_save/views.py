from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import UploadFileForm
from .models import UploadingFileModel
from pprint import pprint
import re
from utils import save_file


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file_field = request.FILES['file']
            file_name = request.FILES['file']._name

            # Get file size from HTTP Header. May be not needed.
            regex_content_length = re.compile(r'^CONTENT_LENGTH$')
            for header in request.META:
                if regex_content_length.match(header):
                    file_size = int(request.META[header])

            instance = UploadingFileModel(name=file_name,
                                          size=file_size,
                                          percents=0,
                                          characters=0,
                                          )
            instance.save()

            import __builtin__
            __builtin__.file_field = file_field
            # start async saving
            save_file.delay(instance)

            # TO DO generate unique URI with uuid
            return HttpResponseRedirect('/file/%d/' % instance.id)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def check_uploading(request, file_id):
    file_uploading = get_object_or_404(UploadingFileModel, pk=file_id)

    c = RequestContext(request, {
        'file_uploading': file_uploading,
        })

    return render_to_response('check_uploading.html', context_instance=c)
