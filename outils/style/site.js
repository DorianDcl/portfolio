// Petites améliorations. Le site reste entièrement lisible sans JavaScript.
(function () {
  "use strict";

  // 1. Adresse de courriel reconstituée (limite la collecte par les robots).
  document.querySelectorAll("a.courriel").forEach(function (lien) {
    var adresse = lien.dataset.u + "@" + lien.dataset.d;
    lien.href = "mailto:" + adresse;
    lien.textContent = adresse;
  });

  // 2. Filtres de la liste des réalisations.
  var formulaire = document.getElementById("filtres");
  var liste = document.getElementById("liste-rea");
  if (formulaire && liste) {
    var lignes = Array.prototype.slice.call(liste.children);
    var compteur = document.getElementById("compteur");
    var aucune = document.getElementById("aucune");
    var filtrer = function () {
      var c = formulaire.competence.value;
      var p = formulaire.periode.value;
      var t = formulaire.technologie.value;
      var visibles = 0;
      lignes.forEach(function (ligne) {
        var ok = (!c || ligne.dataset.competences.split(" ").indexOf(c) !== -1) &&
                 (!p || ligne.dataset.periode === p) &&
                 (!t || ligne.dataset.technologies.split(" ").indexOf(t) !== -1);
        ligne.hidden = !ok;
        if (ok) { visibles += 1; }
      });
      compteur.textContent = visibles + " réalisation" + (visibles > 1 ? "s" : "") +
        (visibles < lignes.length ? " sur " + lignes.length : "");
      aucune.hidden = visibles !== 0;
    };
    formulaire.hidden = false;
    formulaire.addEventListener("change", filtrer);
    formulaire.addEventListener("reset", function () { setTimeout(filtrer, 0); });
    // Filtre transmis par l'adresse, par exemple ?competence=mode-projet
    var parametres = new URLSearchParams(location.search);
    ["competence", "periode", "technologie"].forEach(function (nom) {
      if (parametres.get(nom)) { formulaire[nom].value = parametres.get(nom); }
    });
    filtrer();
  }

  // 3. Agrandissement des captures d'écran.
  var visionneuse = document.getElementById("visionneuse");
  if (visionneuse && typeof visionneuse.showModal === "function") {
    var image = visionneuse.querySelector("img");
    var legende = visionneuse.querySelector("p");
    document.querySelectorAll(".galerie a[data-grand]").forEach(function (lien) {
      lien.addEventListener("click", function (evenement) {
        evenement.preventDefault();
        image.src = lien.dataset.grand;
        image.alt = lien.dataset.legende;
        legende.textContent = lien.dataset.legende;
        visionneuse.showModal();
      });
    });
    visionneuse.addEventListener("click", function (evenement) {
      if (evenement.target === visionneuse) { visionneuse.close(); }
    });
  }
})();
