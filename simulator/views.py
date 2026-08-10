from django.shortcuts import redirect, render, get_object_or_404

from simulator.models import Airport
from simulator.forms import AirportForm

# Create your views here.

def airport_list(request):
    airports = Airport.objects.all()
    return render(request, 'simulator/airport_list.html', {'airports': airports})

def airport_create(request):
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('simulator:airport_list')
    else:
        form = AirportForm()
    return render(request, 'simulator/airport_form.html', {'form': form})


def airport_update(request, pk):
    airport = get_object_or_404(Airport, pk=pk)
    if request.method == "POST":
        form = AirportForm(request.POST, instance=airport)
        if form.is_valid():
            form.save()
            return redirect("simulator:airport_list")
    else:
        form = AirportForm(instnce=airport)
    return render(request, "simulator/airport_form.html", {"form": form})

def airport_delete(request, pk):
    airport = get_object_or_404(Airport, pk=pk)

    if request.method == "POST":
        airport.delete()
        return redirect("simulator:airport_list")

    return render(
        request,
        "simulator/airport_confirm_delete.html",
        {"airport": airport},
    )