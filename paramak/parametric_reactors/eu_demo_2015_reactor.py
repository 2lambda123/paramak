
import paramak


class EuDemoFrom2015PaperDiagram(paramak.Reactor):
    """Creates geometry of a simplified EU DEMO model based on the published
    diagram in Figure 2 of Definition of the basic DEMO tokamak geometry based
    on systems code studies. Published in Fusion Engineering and Design
    http://dx.doi.org/10.1016/j.fusengdes.2015.06.097 . Coordinates extracted
    from the figure are not exact and therefore this model does not
    perfectly represent the reactor.

    Arguments:
        rotation_angle (float): the angle of the sector that is desired.
            Defaults to 360.0.
    """

    def __init__(
        self,
        rotation_angle=360.0,
    ):

        super().__init__([])

        self.rotation_angle = rotation_angle

    def create_solids(self):
        """Creates a 3d solids for each component.

           Returns:
              A list of CadQuery solids: A list of 3D solid volumes

        """

        outboard_pf_coils = paramak.PoloidalFieldCoilSet(
            center_points=[
                (689, -985),
                (1421, -689),
                (1580, -252),
                (1550, 293),
                (1400, 598),
                (621, 811),
            ],
            widths=[
                803 - 599,
                1492 - 1351,
                1628 - 1526,
                1598 - 1503,
                1439 - 1360,
                684 - 563
            ],
            heights=[
                803 - 599,
                1492 - 1351,
                1628 - 1526,
                1598 - 1503,
                1439 - 1360,
                684 - 563
            ],
            rotation_angle=self.rotation_angle,
            stl_filename='outboard_pf_coils.stl',
            stp_filename='outboard_pf_coils.stp',
        )

        pf_coils_1 = paramak.RotateStraightShape(
            points=[
                (263.6088589363423, -881.6221003581469),
                (263.6088589363423, -609.1721122963762),
                (363.04586051526934, -609.1721122963762),
                (363.04586051526934, -881.6221003581469),
            ],
            rotation_angle=self.rotation_angle,
            stl_filename='pf_coils_1.stl',
            stp_filename='pf_coils_1.stp',
        )
        pf_coils_2 = paramak.RotateStraightShape(
            points=[
                (266.2030353910733, -332.3839488581665),
                (357.77071359802824, -332.3839488581665),
                (357.77071359802824, -600.8478453421652),
                (266.2030353910733, -600.8478453421652),
            ],
            rotation_angle=self.rotation_angle,
            stl_filename='pf_coils_2.stl',
            stp_filename='pf_coils_2.stp',
        )
        pf_coils_3 = paramak.RotateStraightShape(
            points=[
                (263.5606400431317, 217.1559887549579),
                (360.3263149381907, 217.1559887549579),
                (360.3263149381907, -316.0372010628879),
                (263.5606400431317, -316.0372010628879),
            ],
            rotation_angle=self.rotation_angle,
            stl_filename='pf_coils_3.stl',
            stp_filename='pf_coils_3.stp',
        )

        pf_coils_4 = paramak.RotateStraightShape(
            points=[
                (262.2297985905187, 493.9315777717868),
                (357.70320714753336, 493.9315777717868),
                (357.70320714753336, 229.49149612970268),
                (262.2297985905187, 229.49149612970268),
            ],
            rotation_angle=self.rotation_angle,
            stl_filename='pf_coils_4.stl',
            stp_filename='pf_coils_4.stp',
        )
        pf_coils_5 = paramak.RotateStraightShape(
            points=[
                (261.01468248161126, 746.6397242654133),
                (356.35307813763615, 746.6397242654133),
                (356.35307813763615, 510.27832556706545),
                (261.01468248161126, 510.27832556706545),
            ],
            rotation_angle=self.rotation_angle,
            stl_filename='pf_coils_5.stl',
            stp_filename='pf_coils_5.stp',
        )

        centre_coils = [
            pf_coils_1,
            pf_coils_2,
            pf_coils_3,
            pf_coils_4,
            pf_coils_5]

        # plasma = paramak.Plasma(
        #     major_radius=185,
        #     minor_radius=57 - 6,  # 3 is a small ofset to avoid overlaps
        #     triangularity=0.31,
        #     elongation=1.97,
        #     rotation_angle=self.rotation_angle,
        #     stp_filename='plasma.stp',
        # )

        # R1 = 511 - 50 / 2
        # R2 = 1340 + 50 / 2
        # coil_thickness = 25
        # tf_coil = paramak.ToroidalFieldCoilPrincetonD(
        #     R1=R1,
        #     R2=R2,
        #     thickness=coil_thickness,
        #     distance=coil_thickness,
        #     number_of_coils=6,
        #     rotation_angle=self.rotation_angle,
        #     stp_filename='tf_coil.stp',
        #     stl_filename='tf_coil.stl',
        # )

        # tf_coil_casing = paramak.TFCoilCasing(
        #     tf_coil,
        #     inner_offset=R2 - 1340,
        #     outer_offset=1500 - R2 - coil_thickness,
        #     vertical_section_offset=25,
        #     distance=100,
        #     rotation_angle=self.rotation_angle,
        #     stp_filename="tf_coil_casing.stp",
        #     stl_filename="tf_coil_casing.stl",
        # )

        vac_vessel = paramak.RotateStraightShape(
            points=[
                (807.3058112219354, 599.9716732776211),
                (944.7007255362573, 596.4005376054217),
                (1066.6077313513304, 548.6554596218273),
                (1176.8939839026452, 468.7827350098197),
                (1252.009375746139, 356.7069172411133),
                (1311.4632710748253, 236.55832094581558),
                (1331.6284122155039, 124.30646127777527),
                (1335.7655932529747, 80.19539107328501),
                (1344.2521184580423, -52.150393961566806),
                (1336.6142457734813, -96.29918743020028),
                (1325.2635183117027, -184.5841999460855),
                (1313.874215735356, -264.8467316209036),
                (1286.7848415296335, -345.1595609812456),
                (1224.659619517079, -485.7541664420229),
                (1162.3222343743978, -582.2251272769284),
                (1072.4518612084566, -666.7503877998998),
                (1013.7308930565716, -699.0289274848848),
                (947.1406015327145, -727.321375592098),
                (813.6899926830206, -727.7489059190513),
                (738.9989270997804, -703.9203774020874),
                (668.1364416374629, -660.0230723610736),
                (609.0297223398928, -612.0768036353835),
                (549.6915523549119, -515.9956498632881),
                (521.8113883005352, -431.84762198174633),
                (517.6742072630645, -387.73655177725584),
                (516.1119151230407, -62.82607771402195),
                (514.4917603111641, 274.11811761081333),
                (533.6539484730619, 370.4507598105283),
                (564.7262032579812, 438.74244233065),
                (607.6120868795008, 499.0493672738471),
                (674.0866530596526, 551.4092579042626),
                (732.8269087688219, 579.6765571687138),
            ],
            rotation_angle=self.rotation_angle,
            stp_filename='vacvessel.stp',
            stl_filename='vacvessel.stl',
        )

        blanket = paramak.RotateMixedShape(
            points=[
                (1028.5051619363035, -506.43908961374075, "spline"),
                (1130.0155759232866, -393.79742288289015, "spline"),
                (1192.275810836831, -281.2815003658492, "spline"),
                (1238.8359741209995, -168.81587553433235, "spline"),
                (1257.92101205376, -56.43827165248217, "spline"),
                (1269.0210012708435, 83.99286633034205, "spline"),
                (1244.8344044363996, 216.28835367966997, "spline"),
                (1205.0441737590018, 328.47734124080523, "spline"),
                (1153.671764932414, 400.5162013324601, "spline"),
                (1074.843518311703, 468.4558000539141, "spline"),
                (988.2423861054414, 520.3252882504712, "spline"),
                (941.0843085454615, 532.2081164555008, "spline"),
                (807.595124581199, 539.8030669696149, "spline"),
                (740.9855455000577, 515.5218592829356, "spline"),
                (670.5280987407093, 475.18311549274034, "spline"),
                (619.7728917472175, 418.862282127315, "spline"),
                (584.8527692840913, 334.5130635036775, "spline"),
                (577.2148965995302, 290.3642700350441, "spline"),
                (574.292831670967, 81.767193745908, "spline"),
                (579.0665020988178, -94.71481033619636, "spline"),
                (579.3751030153657, -158.89465706473618, "spline"),
                (579.8572919474718, -259.17566757808015, "spline"),
                (580.3587684368622, -363.4679185119577, "straight"),
                (686.29567682058, -355.1059282936036, "spline"),
                (670.190566488235, -270.9201771479187, "spline"),
                (657.9911865059497, -182.71061116031922, "straight"),
                (657.4125597874224, -62.3733985443065, "straight"),
                (656.6796326106211, 90.05373743597613, "straight"),
                (652.0409750837601, 238.45705857434393, "spline"),
                (671.3960388185003, 294.67729656872143, "spline"),
                (694.7146955751529, 342.8876281434125, "spline"),
                (725.9412508183462, 379.089387299264, "spline"),
                (765.0757045480802, 403.2825740362764, "spline"),
                (804.2487333923825, 419.4532799322212, "spline"),
                (949.5322586359608, 407.8848122617163, "spline"),
                (1036.1333908422225, 356.0153240651591, "spline"),
                (1067.764984788385, 307.98103438980206, "spline"),
                (1095.4908483844877, 255.92292987253006, "spline"),
                (1115.4631139523237, 183.7834744098276, "spline"),
                (1127.4889059190507, 131.6750722070317, "spline"),
                (1135.5703924211496, 83.56533600338867, "spline"),
                (1128.4147086686944, -60.864467978588436, "spline"),
                (1113.0811006277195, -137.12833365425365, "spline"),
                (1082.0859960719372, -221.46497785651047, "spline"),
                (1031.4658019794351, -305.864494165672, "spline"),
                (945.6554596218276, -418.4558632109989, "straight"),

            ],
            rotation_angle=self.rotation_angle,
            stp_filename="blanket.stp",
            stl_filename="blanket.stl",
        )

        divertor = paramak.RotateMixedShape(
            points=[
                (580.3587684368622, -363.4679185119577, "straight"),
                (678.5035036777448, -367.1647983979668, "straight"),
                (698.2057434436014, -383.14688797319684, "straight"),
                (706.2100797165632, -415.21166249470514, "straight"),
                (698.4950568028651, -443.3154942812033, "straight"),
                (694.7436269110794, -479.42923248738805, "straight"),
                (690.8764716755882, -491.47552817037024, "straight"),
                (726.2209203989679, -495.3735987984752, "straight"),
                (745.6917094774136, -463.22080332730013, "straight"),
                (769.222529364193, -459.1341163784806, "straight"),
                (788.8861940154811, -467.093725112643, "straight"),
                (808.5691462240535, -479.0645742673395, "straight"),
                (863.866572957985, -551.0908599376131, "straight"),
                (891.3995609812453, -563.0365602495477, "straight"),
                (895.1702784303153, -530.9340624638968, "straight"),
                (883.2602118072937, -502.8931027843033, "straight"),
                (886.9923541417953, -462.76812415758457, "straight"),
                (929.9168128778833, -410.48368005545524, "straight"),
                (1036.3937728655599, -514.4364216120463, "straight"),
                (985.8893041167635, -622.9033804444106, "straight"),
                (946.7548503870296, -647.096567181423, "straight"),
                (801.5291878153039, -647.5618207725194, "straight"),
                (675.5814387491815, -575.7618746871029, "straight"),
                (612.3761135287094, -491.72701659798975, "straight"),
                (584.5345245889013, -415.60146955751554, "straight"),
            ],
            rotation_angle=self.rotation_angle,
            stp_filename="divertor.stp",
            stl_filename="divertor.stl",
        )

        self.shapes_and_components = [
            *centre_coils,
            blanket,
            vac_vessel,
            outboard_pf_coils,
            divertor,
            # tf_coil,
            # tf_coil_casing,
        ]
